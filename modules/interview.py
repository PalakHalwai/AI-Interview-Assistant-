from Data.answer_keywords import ANSWER_KEYWORDS
from modules.history import save_history
import random


def load_questions(files, questions_per_file=None):

    if isinstance(files, str):
        files = [files]

    all_questions = []

    for filename in files:

        with open(filename, "r", encoding="utf-8") as file:
            questions = file.read().splitlines()

        if questions_per_file is None:
            all_questions.extend(questions)
        else:
            all_questions.extend(
                random.sample(questions, min(questions_per_file, len(questions)))
            )

    random.shuffle(all_questions)

    return all_questions


def calculate_score(questions, answers):

    total_score = 0

    for question, answer in zip(questions, answers):

        keywords = ANSWER_KEYWORDS.get(question, [])

        answer = answer.lower()

        matches = 0

        for keyword in keywords:
            if keyword.lower() in answer:
                matches += 1

        if len(keywords) > 0:
            question_score = (matches / len(keywords)) * 10
        else:
            if len(answer) >= 15:
                question_score = 6
            else:
                question_score = 3

        total_score += question_score

    final_score = round(total_score / len(questions))

    return final_score


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


def interview(name, filename, interview_title, questions_per_file=None):
    print("\n" + "=" * 50)
    print(f"          {interview_title}")
    print("=" * 50)

    questions = load_questions(filename, questions_per_file)

    if questions_per_file is None:
        questions = random.sample(questions, min(6, len(questions)))

    answers = []

    for number, question in enumerate(questions, start=1):

        display_question = question

        if "|" in question:
            display_question = question.split("|")[0]

        print(f"\nQuestion {number}:")
        print(display_question)

        while True:
            answer = input("Your Answer: ").strip()

            if answer == "":
                print("❌ Answer cannot be empty. Please try again.\n")
            else:
                answers.append(answer)
                break

    score = calculate_score(questions, answers)

    show_report(interview_title, answers, score)

    interview_type = interview_title.replace(" INTERVIEW", "")
    save_history(name, interview_type, score, len(answers))

    input("\nPress Enter to return to the Main Menu...")
