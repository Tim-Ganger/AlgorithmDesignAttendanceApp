import datetime

import IPython

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

URI = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)


class Student(db.Model):

    __tablename__ = 'UserRemap'
    firstName = db.Column(db.String, primary_key=True)
    lastName = db.Column(db.String, primary_key=True)
    advisor = db.Column(db.String)
    grade = db.Column(db.Integer)
    parentEmail = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, first, last, grade, advisor, parentEmail, status):

        self.firstName = first
        self.lastName = last
        self.advisor = advisor
        self.grade = grade
        self.parentEmail = parentEmail
        self.status = status

        def __repr__(self):

            name = self.firstName + " " + self.lastName
            return "Student Info: " + name + ", " + self.advisor

        @property
        def json(self):

            return {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "advisor": self.advisor,
                "grade": self.grade,
                "parentEmail": self.parentEmail,
                "status": self.status
            }


def studentToString(student):

    output = student.firstName + ", "
    output += student.lastName + ", "
    output += str(student.advisor) + ", "
    output += str(student.grade) + ", "
    output += student.parentEmail + ", "
    output += student.status

    return output


def studentFromString(string):

    array = string.split(",")

    if len(array) == 6:

        first = array[0]
        last = array[1]
        advisor = array[2]
        grade = int(array[3])
        parentEmail = array[4]
        status = array[5]
        return Student(first, last, advisor, grade, parentEmail, status)

    else:
        print("Not Propper String")


@app.route("/")
def hello():

    # s = Student("EJ", Eppinger", 12, "Nassar", "parentemail@email.com", "p")
    # print(s)
    return "Hello World!"


def loadFromCSV():

    students = []
    currentStudents = open("current_students.csv", "r")
    currentStudentsStringArray = currentStudents.read().split("\n")

    for string in currentStudentsStringArray:
        students.append(studentFromString(string))

    currentStudents.close()


def exportToCSV(students):

    now = datetime.datetime.now()
    output = open(str(now.year) + "_" + str(now.month) + "_" + str(now.day) + ".csv", "w")

    for student in students:
        output.write(studentToString(student) + "\n")

    output.close()


if __name__ == "__main__":
    app.run()
    IPython.embed()
