from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Barentsburg, Svalbard',
        'salary': '350000'
    },
    {
        'id': 2,
        'title': 'Caretaker',
        'location': 'Grumantbyen, Svalbard',
        'salary': '750000'
    },
    {
        'id': 3,
        'title': 'Office Manager',
        'location': 'Barentsburg, Svalbard'
    },
    {
        'id': 4,
        'title': 'Data Scientist',
        'location': 'Barentsburg, Svalbard',
        'salary': '550000'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

# Show the jobs in JSON
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=true, host="0.0.0.0")