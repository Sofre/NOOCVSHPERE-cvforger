from app.backend.modules.providers.openrouter.provider_conf import get_config


# Register interface - it job is to register and thats it .. doesnt need to know what happening..
class ModelRegistry:
    def __init__(self):
        self.config = get_config()
        self.client = self.config.create_client()

    def get_client(self):
        return self.client

    def get_config(self):
        return self.config

    def close(self):
        return self.client.close()
