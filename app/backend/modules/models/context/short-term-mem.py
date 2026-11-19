from .base import BaseContext

class Short_TermMemoryContext(BaseContext):

    def __init__(self,content:dict):
        super().__init__(content)

    def build(self) -> dict:

        if not self.validate():
            raise ValueError("Invalid system context")

        
        return {

            "type": "short-term", # short-term should be added to the memory context of the chatbot and feed in the long-term for the agents ? 
            "content": self.to_dict()
        }


#    "current_goal": "Improve my CV", -- extract from input promt either with the chatbot should do this as a task or a service
#   "active_task": "Analyze and rewrite backend experience section", -- same with first one 
#    "recent_decisions": [],
#    "temporary_facts": []


shortmem = Short_TermMemoryContext({

        "current_goal" : str # extract from chatbot intrperation
        "active_task" : str # Extract from chatbot intreprtaion
        "status_active_task" : bool # is it active currently
        "recent_decisions": []
        "temporary_facts": []
        



})