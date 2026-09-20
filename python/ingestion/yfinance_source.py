import yfinance as yf 
from ingestion.data_source import DataSource

class YFinanceDataSource(DataSource):
    def __init__(self, ticker:str, period:str="1mo") -> None:
        self.ticker = ticker
        self.period = period

    def get_raw_data(self) -> str:
        df = yf.Ticker(self.ticker).history(self.period)
        df = df.reset_index()
        # Match the shape your DataParser already expects: data, close, volume
        df = df[["Date", "Close", "Volume"]]
        df.columns = ["date", "close","volume"]

        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
        return df.to_csv(index=False)

    def describe(self) -> str:
        return f"yfinance ticker: {self.ticker} ({self.period})"