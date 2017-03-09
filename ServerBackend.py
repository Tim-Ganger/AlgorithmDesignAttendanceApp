from flask import Flask

app = Flask(__name__)


class Student():

    name = ""
    advisor = ""
    grade = 0
    parentEmail = ""

    def __init__(self, name, grade, advisor, parentEmail):
        self.name = name
        self.advisor = advisor
        self.grade = grade
        self.parentEmail = parentEmail


@app.route("/")
def hello():
    s = Student("EJ Eppinger", 12, "Nassar", "parentemail@email.com")
    print(s)
    return "Hello World!"


if __name__ == "__main__":
    app.run()
