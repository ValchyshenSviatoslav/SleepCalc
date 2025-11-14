import datetime

class HistoryManager:
    def __init__(self, filename="history.txt"):
        self.filename = filename

    def save_record(self, results):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()}: {results}\n")
