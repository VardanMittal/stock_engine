from ingestion.data_source import DataSource
from ingestion.csv_source import CSVDataSource
from ingestion.api_source import APIDataSource
from ingestion.yfinance_source import YFinanceDataSource

class DataSourceFactory:
    """The only place in the codebase that knows concrete DataSource
    classes exist. Everything else asks this factory and receives
    back a DataSource — never instantiates one directly."""

    @staticmethod
    def create(source_type: str, **kwargs) -> DataSource:
        if source_type == "csv":
            return CSVDataSource(kwargs["filepath"])
        elif source_type == "api":
            return APIDataSource(kwargs["url"])
        elif source_type == "yfinance":
            return YFinanceDataSource(kwargs["ticker"], kwargs.get("period", "1mo"))
        else:
            raise ValueError(f"Unknown source type: {source_type}")