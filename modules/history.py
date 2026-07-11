import json
import os


def save_history(name, score, total_questions):
    interview = {"name": name, "score": score, "questions_answered": total_questions}

    filename = "history/interview_history.json"

    if os.path.exists(filename):

        with open(filename, "r") as file:
            history = json.load(file)

    else:
        history = []

    history.append(interview)

    with open(filename, "w") as file:
        json.dump(history, file, indent=4)
