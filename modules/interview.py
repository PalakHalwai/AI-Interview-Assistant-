from modules.history import save_history
from ai_evaluator import evaluate_interview
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


def get_feedback(score):

    if score >= 8:
        return "🌟 Excellent! Your answers were detailed and impressive."

    elif score >= 5:
        return "👍 Good effort! Try giving more detailed answers."

    else:
        return "📚 Needs improvement. Consider elaborating on your answers."


def show_report(interview_title, questions, answers, ai_results):

    print("\n" + "=" * 50)
    print(f"          {interview_title} REPORT")
    print("=" * 50)

    print(f"\nQuestions Answered: {len(answers)}")

    # If AI evaluation failed
    if ai_results is None:

        print("\n⚠️ AI Evaluation Unavailable")
        print("Your interview answers were collected successfully.")
        print("Please try the AI evaluation again later.")

        print("\nYour Answers:")

        for number, (question, answer) in enumerate(zip(questions, answers), start=1):

            question_text = question.split("|")[0]

            print(f"\nQuestion {number}")
            print(question_text)

            print("\nYour Answer:")
            print(answer)

        print("\n🎉 Interview Completed!")

        return None

    # Calculate overall score
    scores = [result["score"] for result in ai_results]

    overall_score = round(sum(scores) / len(scores), 1)

    print(f"\nInterview Score: {overall_score}/10")

    print("\nFeedback:")
    print(get_feedback(overall_score))

    print("\nYour Answers:")

    for number, (question, answer, result) in enumerate(
        zip(questions, answers, ai_results), start=1
    ):

        question_text = question.split("|")[0]

        print(f"\nQuestion {number}")
        print(question_text)

        print("\nYour Answer:")
        print(answer)

        print("\nAI Evaluation:")
        print(f"Score: {result['score']}/10")
        print(f"Feedback: {result['feedback']}")

    print("\n🎉 Interview Completed!")

    return overall_score


def interview(name, filename, interview_title, questions_per_file=None):

    print("\n" + "=" * 50)
    print(f"          {interview_title}")
    print("=" * 50)

    questions = load_questions(filename, questions_per_file)

    if questions_per_file is None:
        questions = random.sample(questions, min(6, len(questions)))

    answers = []

    # -----------------------------
    # COLLECT ALL ANSWERS FIRST
    # -----------------------------

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

    # -----------------------------
    # ONE AI REQUEST
    # -----------------------------

    print("\n🤖 Evaluating your complete interview...")
    print("Please wait...\n")

    clean_questions = []

    for question in questions:

        if "|" in question:
            clean_questions.append(question.split("|")[0])

        else:
            clean_questions.append(question)

    ai_results = evaluate_interview(clean_questions, answers)

    # -----------------------------
    # SHOW REPORT
    # -----------------------------

    overall_score = show_report(interview_title, clean_questions, answers, ai_results)

    # -----------------------------
    # SAVE HISTORY
    # -----------------------------

    interview_type = interview_title.replace(" INTERVIEW", "")

    if overall_score is not None:

        save_history(name, interview_type, overall_score, len(answers))

    input("\nPress Enter to return to the Main Menu...")
