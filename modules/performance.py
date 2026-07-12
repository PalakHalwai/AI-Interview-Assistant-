import json
import os


def show_history():

    filename = "history/interview_history.json"

    if not os.path.exists(filename):
        print("\nNo performance history found.")
        input("\nPress Enter to return...")
        return

    with open(filename, "r") as file:
        history = json.load(file)

    print("\n" + "=" * 50)
    print("         PERFORMANCE HISTORY")
    print("=" * 50)

    total_score = 0
    highest_score = 0

    for number, interview in enumerate(history, start=1):

        print(f"\nInterview {number}")
        print(f"Candidate: {interview['name']}")
        print(f"Score: {interview['score']}/10")
        print(f"Questions Answered: {interview['questions_answered']}")
        print("-" * 50)

        total_score += interview["score"]

        if interview["score"] > highest_score:
            highest_score = interview["score"]

    average = total_score / len(history)

    print(f"\nTotal Interviews : {len(history)}")
    print(f"Average Score    : {average:.1f}/10")
    print(f"Highest Score    : {highest_score}/10")

    input("\nPress Enter to return...")
