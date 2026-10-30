from flask import Flask
from uuid import UUID
app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/users")
def users():
    return "Welcome to users Page"

@app.route("/user/<int:id>")
def user(id):
    return f"User ID: {id}"

@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/employ/<uuid:user_id>")
def employ(user_id):
    return str(user_id)

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)