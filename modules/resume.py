CHECKS = [
    ("Education", "Add an Education section."),
    ("Skills", "Include your technical and soft skills."),
    ("Projects", "Mention at least one project."),
    ("Experience", "Include work experience or internships."),
    ("Certifications", "Mention your certifications."),
]


def read_resume(filename):

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def calculate_score(content):

    score = 0

    for keyword, suggestion in CHECKS:
        if keyword.lower() in content.lower():
            score += 20

    return min(score, 100)


def get_suggestions(content):

    suggestions = []

    for keyword, suggestion in CHECKS:
        if keyword.lower() not in content.lower():
            suggestions.append(suggestion)

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
