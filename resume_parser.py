import spacy

nlp = spacy.load("en_core_web_sm")

def parse_resume(file):
    content = file.read().decode('utf-8')
    doc = nlp(content)

    # Extract information
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    experience = [ent.text for ent in doc.ents if ent.label_ == "EXPERIENCE"]
    name = doc.ents[0].text if doc.ents else "Unknown"

    return {
        "name": name,
        "skills": ", ".join(skills),
        "experience": ", ".join(experience)
    }
