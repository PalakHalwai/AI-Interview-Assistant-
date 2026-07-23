def read_resume(filename):

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def calculate_score(content):

    score = 0

    checks = [
        "Education",
        "Skills",
        "Projects",
        "Experience",
        "Certifications",
        "@",  # Email
        "+91",  # Phone (basic check)
        "LinkedIn",
        "GitHub",
    ]

    for item in checks:
        if item.lower() in content.lower():
            score += 10

    if score > 100:
        score = 100

    return score


def get_suggestions(content):

    suggestions = []

    if "Education".lower() not in content.lower():
        suggestions.append("Add an Education section.")

    if "Skills".lower() not in content.lower():
        suggestions.append("Include your technical and soft skills.")

    if "Projects".lower() not in content.lower():
        suggestions.append("Mention at least one project.")

    if "Experience".lower() not in content.lower():
        suggestions.append("Include work experience or internships.")

    if "Certifications".lower() not in content.lower():
        suggestions.append("Mention your certifications.")

    if "@" not in content:
        suggestions.append("Add your email address.")

    if "+91" not in content:
        suggestions.append("Add your phone number.")

    if "linkedin.com" not in content.lower():
        suggestions.append("Add your LinkedIn profile.")

    if "github.com" not in content.lower():
        suggestions.append("Add your GitHub profile (recommended for technical roles).")

    return suggestions


def analyze_resume():

    filename = input("\nEnter resume filename: ")

    filename = "resumes/" + filename

    content = read_resume(filename)

    print("\n----- RESUME CONTENT -----")
    print(content)
    print("--------------------------")

    score = calculate_score(content)
    suggestions = get_suggestions(content)

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
