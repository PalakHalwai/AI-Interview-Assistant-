from modules.interview import interview


def start_mock_interview(name):

    while True:

        print("\n" + "=" * 50)
        print("          MOCK INTERVIEW")
        print("=" * 50)

        print("\nChoose Interview Type\n")
        print("1. HR Interview")
        print("2. Technical Interview")
        print("3. Mixed Interview")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            interview(name, "data/hr_questions.txt", "HR MOCK INTERVIEW")
            break

        elif choice == "2":
            interview(
                name,
                [
                    "data/python_questions.txt",
                    "data/python_questions.txt",  # Python twice
                    "data/sql_questions.txt",
                    "data/java_questions.txt",
                    "data/cpp_questions.txt",
                    "data/aptitude_questions.txt",
                ],
                "TECHNICAL MOCK INTERVIEW",
                questions_per_file=1,
            )

        elif choice == "3":
            interview(
                name,
                [
                    "data/hr_questions.txt",
                    "data/hr_questions.txt",  # HR twice
                    "data/python_questions.txt",
                    "data/sql_questions.txt",
                    "data/java_questions.txt",
                    "data/aptitude_questions.txt",
                ],
                "MIXED MOCK INTERVIEW",
                questions_per_file=1,
            )

        elif choice == "0":

            break

        else:

            print("\nInvalid choice.")
