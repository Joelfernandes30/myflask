from flask import Flask,render_template,jsonify

app = Flask(__name__)


JOBS = [
  {
    'id':1,
    'title': 'DevOps Engineer',
    'location': 'Bengaluru',
    'Salary': 'Rs. 800000'
  },
{
    'id':2,
    'title': 'Data Scientist',
    'location': 'Delhi',
    'Salary': 'Rs. 1200000'
  },
{
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Mumbai',
    'Salary': 'Rs. 600000'
  },
{
    'id': 4,
    'title': 'Full Stack Developer',
    'location': 'Remote',
    'Salary': 'Rs. 1000000'
  }
]
@app.route('/')
def hello():
  return render_template("index.html", jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
  app.run(debug=True)