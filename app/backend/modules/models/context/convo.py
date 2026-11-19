from .base import BaseContext


class ConvoContext(BaseContext):
    def build(self) -> dict:
        if not self.validate():
            raise ValueError("Invalid conversation context")
        if not isinstance(self.content.get("messages"), list):
            raise ValueError("Conversation context must contain a messages list")
        return {
            "type": "conversation",
            "content": self.to_dict(),
        }


convo = ConvoContext(
    {
        "conversation_id": "conv_001",
        "user_id": "user_001",
        "messages": [
            {"role": "user", "content": "Help me improve my CV."},
            {"role": "assistant", "content": "Let's start with your experience."},
        ],
        "metadata": {
            "created_at": None,
            "updated_at": None,
            "message_count": 2,
        },
    }
)