import random


def hr_interview():
    print("\n" + "=" * 50)
    print("              HR INTERVIEW")
    print("=" * 50)

    with open("data/hr_questions.txt", "r") as file:
        questions = file.read().splitlines()
        TOTAL_QUESTIONS = 4
        questions = random.sample(questions, TOTAL_QUESTIONS)

    answers = []

    for i in range(len(questions)):
        print(f"\nQuestion {i + 1}:")
        print(questions[i])

        while True:
            answer = input("Your Answer: ").strip()

            if answer == "":
                print("❌ Answer cannot be empty. Please try again.\n")
            else:
                answers.append(answer)
                break

    print("\n" + "=" * 50)
    print("          HR INTERVIEW REPORT")
    print("=" * 50)

    print(f"\nQuestions Answered: {len(answers)}")

    score = 0

    for answer in answers:
        if len(answer) >= 10:
            score += 3
        else:
            score += 1

    if score > 10:
        score = 10

    print(f"\nInterview Score: {score}/10")

    print("\nFeedback:")

    if score >= 8:
        print("🌟 Excellent! Your answers were detailed and impressive.")
    elif score >= 5:
        print("👍 Good effort! Try giving more detailed answers.")
    else:
        print("📚 Needs improvement. Consider elaborating on your answers.")

    print("\nYour Answers:")

    for i in range(len(answers)):
        print(f"{i + 1}. {answers[i]}")

    print("\n🎉 Interview Completed!")
    input("\nPress Enter to return to the Main Menu...")
