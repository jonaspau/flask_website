from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)


@app.route('/job/<id>')
def show_job_listing(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('job_listing.html', job = job)


@app.route('/job/<id>/apply', methods = ['POST', 'GET'])
def apply_for_position(id):
    data = request.form
    if not data:
        return "Not Found", 404
    job = load_job_from_db(id)
    # show thank you
    return render_template('application_submitted.html', application=data, job=job)
    # store in db
    # send an email
    

# Show the jobs in JSON
@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")