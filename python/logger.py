import datetime

class Logger:
    """Single shared logger instance. Every modeule that logs uses the same instance - no risk of duplicate handlers or inconsistent state"""

    _instance = None
    logs: list[str]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message:str):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] :  {message}"

        self.logs.append(entry)
        print(entry)