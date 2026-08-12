import json
import os

SETTINGS_FILE = "settings.json"
DEFAULT_QUESTIONS = 6


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {"question_count": DEFAULT_QUESTIONS}

    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)

        question_count = settings.get("question_count", DEFAULT_QUESTIONS)

        if not isinstance(question_count, int) or not 1 <= question_count <= 10:
            question_count = DEFAULT_QUESTIONS

        return {"question_count": question_count}

    except (json.JSONDecodeError, OSError):
        return {"question_count": DEFAULT_QUESTIONS}


settings = load_settings()
question_count = settings["question_count"]


def save_settings():
    with open(SETTINGS_FILE, "w") as file:
        json.dump({"question_count": question_count}, file, indent=4)


def settings_menu():
    global question_count

    while True:
        print("\n" + "=" * 50)
        print("                 SETTINGS")
        print("=" * 50)

        print(f"\nCurrent number of questions: {question_count}")

        print("\n1. Change Number of Questions")
        print("2. Reset to Default")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            while True:
                try:
                    number = int(input("Enter number of questions (1-10): ").strip())

                    if 1 <= number <= 10:
                        question_count = number
                        save_settings()

                        print(f"\n✓ Number of questions set to {question_count}.")
                        break

                    print("\nPlease enter a number between 1 and 10.")

                except ValueError:
                    print("\nPlease enter a valid number.")

        elif choice == "2":
            question_count = DEFAULT_QUESTIONS
            save_settings()

            print(f"\n✓ Number of questions reset to {DEFAULT_QUESTIONS}.")

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please try again.")


def get_question_count():
    return question_count
