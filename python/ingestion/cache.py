class DataCache:
    """Responsible only to storing and retreving already fetched data"""

    def __init__(self) -> None:
        self._store: dict[str, list[dict]] = {}

    def get(self, key:str):
        return self._store.get(key)

    def set(self,key:str, value:list[dict]):
        self._store[key] = value