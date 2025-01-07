import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arihantjcc@09",  # replace with your MySQL password
        database="job_matcher"  # replace with your database name
    )

def insert_candidate(candidate_data):
    db = connect_db()
    cursor = db.cursor()
    sql = """
        INSERT INTO candidates (name, skills, experience)
        VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (candidate_data["name"], candidate_data["skills"], candidate_data["experience"]))
    db.commit()
    candidate_id = cursor.lastrowid
    db.close()
    print(f"Candidate added with ID: {candidate_id}")  # This line prints the output
    return candidate_id

def get_all_jobs():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    db.close()
    print("Available jobs:", jobs)  # This line prints the output
    return jobs

def match_candidate_to_jobs(candidate_skills, jobs):
    matched_jobs = []
    for job in jobs:
        job_skills = job['required_skills'].split(',')
        if set(candidate_skills).intersection(set(job_skills)):
            matched_jobs.append(job['id'])
    print(f"Matched jobs for candidate {candidate_skills}: {matched_jobs}")  # This line prints the output
    return matched_jobs

# Example: Insert a candidate and match them to jobs
candidate_data = {"name": "Arihant Jain", "skills": "Python,SQL,Machine Learning", "experience": "3 years"}
insert_candidate(candidate_data)

# Fetch all jobs
jobs = get_all_jobs()


# Match the candidate to jobs
candidate_skills = ["Python", "SQL", "Machine Learning"]
match_candidate_to_jobs(candidate_skills, jobs)
