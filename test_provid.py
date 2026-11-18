from app.backend.modules.models.services.model_reg import ModelService

model_service = ModelService()

messages = [
    {
        "role": "system",
        "content": "You are a helpful Python assistant."
    },
    {
        "role": "user",
        "content": "What can the word Kacinga mean ? "
    }
]

result = model_service.execute(messages)

print(result)