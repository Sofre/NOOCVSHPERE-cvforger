import os
import tomllib
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator
from openrouter import OpenRouter

load_dotenv()
CONFIG_PATH = Path(__file__).resolve().parent / "provider-conf.toml"
# Define the baseline model - this class create a configuration object and methods to load the env and map and send request for model
class OpenRouterConfig(BaseModel):
    api_key: str
    primary_model : str
    fallback_models : list[str]
    temperature: float = 0.2
    top_p: float = 0.95
    max_tokens: int = 8192

    # Create a connection with OpenRouter -- thats why its called create a client 
    @field_validator("api_key")
    @classmethod
    def validate_api_key(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("OPENROUTER_API_KEY is missing or empty in your .env file.")
        return value

    # Make sure both methods below are indented inside OpenRouterConfig!
    def create_client(self) -> OpenRouter:
        return OpenRouter(api_key=self.api_key)



    # Request these models and its configurations kwarg(keywordarguments)
    def to_request_kwargs(self) -> dict:
        return {
            "model":self.primary_model,
            "models":self.fallback_models,
            "temperature":self.temperature,
            "top_p":self.top_p,
            "max_tokens":self.max_tokens

            }


# GET Configuration values by raw byte transforming into a pydir map  and return validation ( check if the conf values are set before API contacting) 
def get_config() -> OpenRouterConfig:
    with open(CONFIG_PATH, "rb") as f:
        raw_config = tomllib.load(f)
    
    return OpenRouterConfig(
        api_key=os.getenv("OPENROUTER_API_KEY", ""),
        **raw_config["openrouter"] # {openrouter:base_url,primary_model,fallback_models(list),temperature,top_p,max_tokens}
        # ** dir unpacking command but it remaps key pair value by the model 
    )
