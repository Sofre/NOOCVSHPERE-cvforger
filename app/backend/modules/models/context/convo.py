from .base import BaseContext

class ConvoContext(BaseContext):

    def __init__(self,content:dict):
        super().__init__(content)
    
    def build(self):

        if not self.validate():
            raise ValueError("Invalid content !")
        

        return {

            "type:" "conversation"
            "content" : self.to_dist()

        }


convo = ConvoContext({
# Conversational context, each convo is mapped to user and its convo id. so it means each convo id can belong to one user.
{
    "conversation_id": "conv_001",
    "user_id": "user_001",
    "messages": [
        {
            "role": "user",
            "content": "Help me improve my CV."
        },
        {
            "role": "assistant",
            "content": "Let's start with your experience."
        }
    ],
    "metadata": {
        "created_at": None,
        "updated_at": None,
        "message_count": 2
    }
}


    })