def hr_interview():
    print("\n" + "=" * 50)
    print("              HR INTERVIEW")
    print("=" * 50)

    questions = [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths?"
    ]

    answers = []

    for question in questions:
        print(f"\n{question}")
        answer = input("Your Answer: ")
        answers.append(answer)

    print("\n🎉 Interview Completed!")
    print("\nYour Answer:")
    for answer in answers:
        print (answer)