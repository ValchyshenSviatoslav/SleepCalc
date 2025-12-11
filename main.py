from calculator import SleepCalculator
from ui import UserInterface
from history import HistoryManager

def main():
    ui = UserInterface()
    history = HistoryManager()
    calculator = SleepCalculator()

    mode = ui.ask_mode()
    if mode == "sleep":
        sleep_time = ui.get_time_input("Введіть час засинання (год:хв): ")
        results = calculator.calculate_by_sleep(sleep_time)
    else:
        wake_time = ui.get_time_input("Введіть час пробудження (год:хв): ")
        results = calculator.calculate_by_wake(wake_time)

    ui.display_results(results)
    history.save_record(results)

if __name__ == "__main__":
    main()

# commit for test
# test commit from dev branch
