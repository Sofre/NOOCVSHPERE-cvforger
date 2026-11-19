from app.backend.modules.models.services.model_registry import ModelRegistry

registry = ModelRegistry()
# Registering service
class ModelService:

    def __init__(self):
        self.client = registry.get_client()
        self.config = registry.get_config()

    
    def execute(self,messages):
        kwargs = self.config.to_request_kwargs()

        response = self.client.chat.send(
            messages=messages,
            **kwargs
        )
        return self.map(response)

   # Return and map kwargs to show if outbound contract is correct -- will be patched
    def map(self, response):
        choice = response.choices[0]
        message = choice.message
        usage = response.usage
        
        return {
            "status": "success",
            "model": response.model,
            "role": message.role,
            "content": message.content,
            "finish_reason": choice.finish_reason,
            "usage": {
                "prompt_tokens": usage.prompt_tokens,
                "completion_tokens": usage.completion_tokens,
                "total_tokens": usage.total_tokens
        }
    }




    # register the model
    # map the primary model 
    # add in status and role 

    # connect to context
    # connect to memory 
    # connect to tool
    # connect and register to orchestrator
    # expose points ?


