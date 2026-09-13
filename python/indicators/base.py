from abc import ABC, abstractmethod

class Indicator(ABC):
     """Base contract for all indicators. New indicators extend this,
    nobody ever needs to modify this file itself."""

     @abstractmethod
     def calculate(self, prices:list[float]) -> float:
          """Take a list of closing price returns the indicator value"""
          pass

     @abstractmethod
     def name(self) -> str:
          pass