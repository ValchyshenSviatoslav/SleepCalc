from datetime import datetime, timedelta

class SleepCalculator:
    def calculate_by_sleep(self, sleep_time_str):
        try:
            sleep_time = datetime.strptime(sleep_time_str, "%H:%M")
        except ValueError:
            return ["Помилка: введіть час у форматі ГГ:ХХ"]

        cycles = []
        for i in range(1, 7):
            wake_time = sleep_time + timedelta(minutes=90 * i)
            cycles.append(wake_time.strftime("%H:%M"))
        return cycles

    def calculate_by_wake(self, wake_time_str):
        try:
            wake_time = datetime.strptime(wake_time_str, "%H:%M")
        except ValueError:
            return ["Помилка: введіть час у форматі ГГ:ХХ"]

        cycles = []
        for i in range(6, 0, -1):
            sleep_time = wake_time - timedelta(minutes=90 * i)
            cycles.append(sleep_time.strftime("%H:%M"))
        return cycles
