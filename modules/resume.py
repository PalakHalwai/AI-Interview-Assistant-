def read_resume(filename):

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def calculate_score(content):

    score = 0

    if "Education" in content:
        score += 20

    if "Skills" in content:
        score += 20

    if "Projects" in content:
        score += 20

    if "Experience" in content:
        score += 20

    if "Certifications" in content:
        score += 20

    return score


def get_suggestions(content):

    suggestions = []

    if "Education" not in content:
        suggestions.append("Add an Education section.")

    if "Skills" not in content:
        suggestions.append("Add a Skills section.")

    if "Projects" not in content:
        suggestions.append("Mention your projects.")

    if "Experience" not in content:
        suggestions.append("Include work or internship experience if available.")

    if "Certifications" not in content:
        suggestions.append("Add your certifications.")

    return suggestions


def analyze_resume():

    filename = input("\nEnter resume filename: ")

    filename = "resumes/" + filename

    content = read_resume(filename)

    score = calculate_score(content)

    suggestions = get_suggestions(content)

    print("\n" + "=" * 50)
    print("          RESUME ANALYSIS")
    print("=" * 50)

    print(f"\nResume Score: {score}/100")

    if len(suggestions) == 0:
        print("\n🎉 Excellent Resume!")
    else:
        print("\nSuggestions:")

        for suggestion in suggestions:
            print(f"• {suggestion}")

    input("\nPress Enter to return...")
