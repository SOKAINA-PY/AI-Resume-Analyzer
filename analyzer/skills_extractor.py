import json

def load_skills(file_path="data/skills.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_skills(text, skills_database):
    text = text.lower()

    detected_skills = []

    for category, skills in skills_database.items():
        for skill in skills:
            if skill.lower() in text:
                detected_skills.append(skill)

    return sorted(list(set(detected_skills)))