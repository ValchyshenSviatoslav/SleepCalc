class UserInterface:
    def ask_mode(self):
        mode = input("Режим (sleep/wake): ").strip().lower()
        return "sleep" if mode == "sleep" else "wake"

    def get_time_input(self, prompt):
        return input(prompt).strip()

    def display_results(self, results):
        print("\nРекомендований час:")
        for time in results:
            print(f" - {time}")
