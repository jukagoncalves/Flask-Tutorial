from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        "Python",
        "Flask",
        "FastAPI",
        "Django"
    ]

    student = {
        "name":"Juka",
        "course":"Flask",
        "city":"SSP"
    }
    return render_template("index.html", courses=courses,student=student)

if __name__ == "__main__":
    app.run(debug=True)