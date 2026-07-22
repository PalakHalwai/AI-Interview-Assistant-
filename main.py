import modules.interview
import modules.aptitude
import modules.performance
import modules.resume

def welcome():
    print("=" * 50)
    print("         AI INTERVIEW ASSISTANT")
    print("=" * 50)
    print()


def menu():
    print("\nChoose an option:")
    print("1. HR Interview")
    print("2. Python Interview")
    print("3. C/C++ Interview")
    print("4. Java Interview")
    print("5. SQL Interview")
    print("6. Aptitude Test")
    print("7. Resume Analysis")
    print("8. Mock Interview")
    print("9. Performance History")
    print("10. Settings")
    print("0. Exit")


welcome()

name = input("Enter your name: ").strip().title()

print(f"\nWelcome, {name}!")

while True:
    menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        modules.interview.interview(name, "data/hr_questions.txt", "HR INTERVIEW")

    elif choice == "9":
        modules.performance.show_history()

    elif choice == "2":
        modules.interview.interview(
            name, "data/python_questions.txt", "PYTHON INTERVIEW"
        )

    elif choice == "3":
        modules.interview.interview(name, "data/cpp_questions.txt", "C/C++ INTERVIEW")

    elif choice == "4":
        modules.interview.interview(name, "data/java_questions.txt", "JAVA INTERVIEW")
    elif choice == "5":
        modules.interview.interview(name, "data/sql_questions.txt", "SQL INTERVIEW")

    elif choice == "6":
         modules.aptitude.aptitude_test(name)

    elif choice == "7":
         modules.resume.analyze_resume()

    elif choice == "0":
        print("\nThank you for using AI Interview Assistant.")
        break

    else:
        print("\n🚧 This feature is under development.\n")
