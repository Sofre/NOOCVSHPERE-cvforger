from typing import Any, Mapping

# Dont run 
class ContextBuilderService:
    def __init__(
        self,
        *,
        system: Mapping[str, Any],
        roles: Mapping[str, Mapping[str, Any]],
        tasks: Mapping[str, Mapping[str, Any]],
    ) -> None:
        self.system = system
        self.roles = roles
        self.tasks = tasks

   CHATBOT_ROLE_ID = "noocvsphere_assistant"

def build(self, *, task_id, available_inputs, conversation_context=None):
    task = self.tasks.get(task_id)
    if task is None:
        raise ValueError(f"Unknown task: {task_id}")

    role_id = task["role_id"]
    role = self.roles.get(role_id)
    if role is None:
        raise ValueError(f"Unknown role: {role_id}")

    context = {
        "system": self.system,
        "role": role,
        "task": task,
        "inputs": {
            name: available_inputs[name]
            for name in task.get("inputs", [])
            if name in available_inputs
            and name != "conversation_history"
        },
    }

    if role_id == CHATBOT_ROLE_ID:
        if conversation_context is None:
            raise ValueError("Chatbot context requires the current conversation")
        context["conversation"] = conversation_context.build()

    return context