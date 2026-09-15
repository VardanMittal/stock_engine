from strategies.interfaces import Predictable, Trainable


class LSTMStrategy(Predictable, Trainable):

    def __init__(self):
        self.is_trained = False

    def train(self, prev_data=list[dict]) -> None:
        # placeholder — real LSTM training comes later
        print(f"Training on {len(prev_data)} rows...")
        self.is_trained = True

    def predict(self, prices: list[float]) -> str:
        if not self.is_trained:
            return "hold"  # can't predict responsibly before training
        # placeholder logic until real model exists
        return "hold"

    def name(self) -> str:
        return "LSTM (stub)"