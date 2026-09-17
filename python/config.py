class Config:
    """Single shared source of app-wide settings. No matter how many times Config() is called across the codebase, it returns the same instance - settings loaded once, shared everywhere"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self,config_path: str="config.json"):
        if self._initialized:
            return
        self.config_path =config_path
        self.settings = self._load_settings()
        self._initialized = True

    def _load_settings(self) -> dict:
        import json, os
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)

        return {
            "intial_cash":10000.0,
            "default_strategy":"ma_crossover",
            "log_level":"INFO"
        }

    def get(self, key:str, default=None):
        return self.settings.get(key, default)