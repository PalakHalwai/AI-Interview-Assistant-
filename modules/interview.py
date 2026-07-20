from modules.history import save_history
import random


def load_questions(filename):

    with open(filename, "r", encoding="utf-8") as file:
        questions = file.read().splitlines()

    TOTAL_QUESTIONS = 6
    questions = random.sample(questions, TOTAL_QUESTIONS)

    return questions


def calculate_score(answers):

    score = 0

    for answer in answers:
        if len(answer) >= 10:
            score += 3
        else:
            score += 1

    if score > 10:
        score = 10

    return score


def get_feedback(score):
    if score >= 8:
        return "🌟 Excellent! Your answers were detailed and impressive."
    elif score >= 5:
        return "👍 Good effort! Try giving more detailed answers."
    else:
        return "📚 Needs improvement. Consider elaborating on your answers."


def show_report(interview_title, answers, score):
    print("\n" + "=" * 50)
    print(f"          {interview_title} REPORT")
    print("=" * 50)

    print(f"\nQuestions Answered: {len(answers)}")
    print(f"\nInterview Score: {score}/10")

    print("\nFeedback:")
    feedback = get_feedback(score)
    print(feedback)

    print("\nYour Answers:")

    for number, answer in enumerate(answers, start=1):
        print(f"{number}. {answer}")

    print("\n🎉 Interview Completed!")


def interview(name, filename, interview_title):
    print("\n" + "=" * 50)
    print(f"          {interview_title}")
    print("=" * 50)

    questions = load_questions(filename)
    answers = []

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}:")
        print(question)

        while True:
            answer = input("Your Answer: ").strip()
            if answer == "":
                print("❌ Answer cannot be empty. Please try again.\n")
            else:
                answers.append(answer)
                break
    score = calculate_score(answers)
    show_report(interview_title, answers, score)

    interview_type = interview_title.replace(" INTERVIEW", "")
    save_history(name, interview_type, score, len(answers))
    input("\nPress Enter to return to the Main Menu...")
