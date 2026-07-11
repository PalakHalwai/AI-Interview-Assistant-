import modules.hr

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

name = input("Enter your name: ")

print(f"\nWelcome, {name}!")

while True:
    menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        modules.hr.hr_interview()

    elif choice == "0":
        print("\nThank you for using AI Interview Assistant.")
        break

    else:
        print("\n🚧 This feature is under development.\n")