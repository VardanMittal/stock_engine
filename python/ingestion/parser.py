import csv 
import io

class DataParser:
    "Responsible only to parse the data into a structured format"

    def parse_csv(self, raw_text: str) -> list[dict]:
        reader = csv.DictReader(io.StringIO(raw_text))
        return list(reader)