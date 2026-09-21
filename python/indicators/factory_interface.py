from abc import ABC, abstractmethod
from indicators.base import Indicator

class IndicatorFactory(ABC):
    """A family of related indicators. Each concrete factory produces
    one consistent 'kind' of indicator — trend, momentum, etc."""

    @abstractmethod
    def create_primary(self) -> Indicator:
        """The main default indicator for this family"""
        pass

    @abstractmethod
    def create_secondary(self) -> Indicator:
        "A supporting indicator for this family, meant to be used alongside the primary one"
        pass

    