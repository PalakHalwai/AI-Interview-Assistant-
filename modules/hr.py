def hr_interview():
    print("\n" + "=" * 50)
    print("              HR INTERVIEW")
    print("=" * 50)

    questions = [
        "Tell me about yourself?",
        "Why should we hire you?",
        "What are your strengths?"
    ]

    answers = []

    for i in range(len(questions)):
        print(f"\nQuestion {i + 1}:")
        print(questions[i])

        answer = input("Your Answer: ")
        answers.append(answer)

    print("\n" + "=" * 50)
    print("          HR INTERVIEW REPORT")
    print("=" * 50)

    print(f"\nQuestions Answered: {len(answers)}")

    print("\nYour Answers:")

    for i in range(len(answers)):
        print(f"{i + 1}. {answers[i]}")

    print("\n🎉 Interview Completed!")