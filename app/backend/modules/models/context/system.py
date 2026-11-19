from .base import BaseContext

class SystemContext(BaseContext):

    def __init__(self,content:dict):
        super().__init__(content)

    def build(self) -> dict:

        if not self.validate():
            raise ValueError("Invalid system context")

        
        return {

            "type": "System",
            "content": self.to_dict()
        }


system = SystemContext({
    "identity": "NOOSPHERE",

    "description": (
        "An AI-powered career assistant that helps candidates "
        "analyze job opportunities and create tailored "
        "application documents."
    ),

    "instructions": [
        "Act professionally and communicate clearly.",
        "Prioritize accuracy, relevance, and transparency.",
        "Never fabricate candidate qualifications or experience.",
        "Never present assumptions as verified facts.",
        "Treat candidate-provided information as the source "
        "of truth for candidate qualifications.",
        "Treat job descriptions as the source of truth for "
        "employer requirements.",
        "Preserve factual consistency across all outputs.",
        "Ask for clarification when essential information is missing.",
        "Explain reasoning behind evaluations and recommendations.",
        "Never claim certainty when available information "
        "does not support it."
    ]
})


result = system.build()
printableresutl = self.contet 
print(result)
print(result["type"])
print(printableresult)