from flask import Flask, request, jsonify
from database import connect_db, get_all_jobs, insert_candidate, match_candidate_to_jobs
from resume_parser import parse_resume
from job_matcher import match_jobs

app = Flask(__name__)

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    job_id = request.form['job_id']

    # Parse resume and extract details
    resume_data = parse_resume(file)

    # Insert candidate into the database
    candidate_id = insert_candidate(resume_data)

    # Match candidate to jobs
    matches = match_jobs(candidate_id, job_id)

    return jsonify(matches)

@app.route('/jobs', methods=['GET'])
def list_jobs():
    jobs = get_all_jobs()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
