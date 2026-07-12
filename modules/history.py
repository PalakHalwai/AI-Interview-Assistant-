import json
import os
from datetime import datetime

def save_history(name, interview_type, score, total_questions):

    now = datetime.now()

    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%I:%M %p")
    interview = {
    "name": name,
    "interview_type": interview_type,
    "score": score,
    "questions_answered": total_questions,
    "date": current_date,
    "time": current_time
}

    filename = "history/interview_history.json"

    if os.path.exists(filename):

        with open(filename, "r") as file:
            history = json.load(file)

    else:
        history = []

    history.append(interview)

    with open(filename, "w") as file:
        json.dump(history, file, indent=4)
