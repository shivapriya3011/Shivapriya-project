job_description = """
We are hiring a Machine Learning Engineer with minimum 3 years experience.
Required skills include Python, Machine Learning, Deep Learning,
TensorFlow, and SQL.
Bachelor's degree in Computer Science or related field is required.
"""
resumes = {
    "Candidate_1": """
    John Doe
    4 years of experience in Machine Learning and Deep Learning.
    Skilled in Python, TensorFlow, SQL and Data Analysis.
    Bachelor's degree in Computer Science.
    """,

    "Candidate_2": """
    Jane Smith
    2 years experience in Web Development.
    Skills include HTML, CSS, JavaScript, and React.
    Bachelor's degree in Information Technology.
    """,

    "Candidate_3": """
    Robert Brown
    5 years of experience in Data Science and Machine Learning.
    Skilled in Python, Deep Learning, SQL and Scikit-learn.
    Master's degree in Computer Science.
    """
}
def preprocess_text(text):
    text = text.lower()
    cleaned_text = ""

    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char

    return cleaned_text


processed_jd = preprocess_text(job_description)

processed_resumes = {}
for name in resumes:
    processed_resumes[name] = preprocess_text(resumes[name])
required_skills = ["python", "machine learning", "deep learning", "tensorflow", "sql"]

def calculate_similarity(resume_text, jd_text):
    match_count = 0

    for skill in required_skills:
        if skill in resume_text:
            match_count += 1

    similarity_score = match_count / len(required_skills)
    return similarity_score

results = []

for name in processed_resumes:
    score = calculate_similarity(processed_resumes[name], processed_jd)
    results.append((name, score))
for i in range(len(results)):
    for j in range(i + 1, len(results)):
        if results[i][1] < results[j][1]:
            results[i], results[j] = results[j], results[i]
def analyze_skills(resume_text):
    matched = []
    missing = []

    for skill in required_skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing

print("===================================================")
print("     AI-BASED RESUME SCREENING SYSTEM OUTPUT")
print("===================================================\n")

rank = 1
for result in results:
    name = result[0]
    score = result[1]

    matched_skills, missing_skills = analyze_skills(processed_resumes[name])

    print("Rank:", rank)
    print("Candidate Name:", name)
    print("Match Score:", round(score, 2))
    print("Matched Skills:", matched_skills)
    print("Missing Skills:", missing_skills)
    print("---------------------------------------------------")

    rank += 1
