from abc import ABC, abstractmethod

class DataSource(ABC):
    """Common contract everydata source should honors. The rest of the codebase 
    depends on this, never on a concrete source class"""

    @abstractmethod
    def get_raw_data(self) -> str:
        """Returns raw data as text (CSV text, JSON text, etc.) —
        parsing happens downstream, this only fetches."""
        pass

    @abstractmethod
    def describe(self) -> str:
        pass