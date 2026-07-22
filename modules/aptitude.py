import random
from modules.history import save_history

def load_questions(filename):

    with open(filename, "r", encoding="utf-8") as file:
        questions = file.read().splitlines()

    questions = random.sample(questions, 4)

    return questions


def ask_questions(questions):

    score = 0

    for number, item in enumerate(questions, start=1):

        question, correct_answer = item.split("|")

        print("\n" + "=" * 50)
        print(f"Question {number}")
        print(question)

        user_answer = input("Your Answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")
            print(f"Correct Answer: {correct_answer}")

    return score


def aptitude_test(name):

    print("\n" + "=" * 50)
    print("             APTITUDE TEST")
    print("=" * 50)

    questions = load_questions("data/aptitude_questions.txt")

    score = ask_questions(questions)

    print("\n" + "=" * 50)
    print("             TEST REPORT")
    print("=" * 50)

    print(f"\nFinal Score: {score}/4")

    if score == 4:
        print("🌟 Excellent!")
    elif score >= 2:
        print("👍 Good Job!")
    else:
        print("📚 Keep Practicing!")
    save_history(name, "APTITUDE", score, 4)
    input("\nPress Enter to return...")
