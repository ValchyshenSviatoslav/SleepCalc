from datetime import datetime, timedelta

class SleepCalculator:
    def __init__(self, cycle_length=90):
        self.cycle_length = cycle_length  # хвилини

    def calculate_by_sleep(self, sleep_time_str):
        sleep_time = datetime.strptime(sleep_time_str, "%H:%M")
        return [(sleep_time + timedelta(minutes=self.cycle_length * i)).strftime("%H:%M")
                for i in range(1, 7)]

    def calculate_by_wake(self, wake_time_str):
        wake_time = datetime.strptime(wake_time_str, "%H:%M")
        return [(wake_time - timedelta(minutes=self.cycle_length * i)).strftime("%H:%M")
                for i in reversed(range(1, 7))]
