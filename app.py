from flask import Flask,render_template,jsonify
from database import load_jobs_from_db


app = Flask(__name__)





@app.route('/')
def hello():
    global jobs
    jobs = load_jobs_from_db()
    return render_template("index.html", jobs=jobs)

@app.route("/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == '__main__':
  app.run(debug=True)