import datetime

import IPython

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

URI = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)


class Student(db.Model):

    __tablename__ = 'StudentTable'
    firstName = db.Column(db.String, unique = False, primary_key = True)
    lastName = db.Column(db.String)
    advisor = db.Column(db.String)
    grade = db.Column(db.String)

    status = db.Column(db.String)

    def __init__(self, first, last, grade, advisor, status):

        self.firstName = first
        self.lastName = last
        self.advisor = advisor
        self.grade = grade

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
    output += student.status

    return output


def studentFromString(string):

    array = string.split(",")

    if len(array) == 4:

        last = array[0]
        first = array[1]
        advisor = array[3]
        grade = array[2]
        status = "p"
        return Student(first, last, advisor, grade, status)

    else:
        print("Not Proper String")


@app.route("/")
def hello():

    # s = Student("EJ", Eppinger", 12, "Nassar", "parentemail@email.com", "p")
    # print(s)
    return "Hello World!"

@app.route("/test")
def testingSearch():
    s = Student("EJ", "NSMYTDM", 12, "Nassar", "p")
    db.session.add(s)
    db.session.commit()
    print(studentsInAdvisory("Nassar"))
    return "If you can read this, the code ran properly. O frabjuous day, O frabjuous day!"
    #return studentsInAdvisory(s.advisor)

def students():
    data = [student.json for student in Student.query.all()]
    return jsonify(data)

def studentsInAdvisory(advisor):
    data = [Student.json for Student in Student.query.filter(Student.advisor == advisor).all()]
    return data

@app.route("/students/<student>", methods=["GET","POST"])
def add_student(student):
    #advisor = request.json["advisor"]
    student_record = Student(student, "LastName", 11, "Nassar", "p")
    db.session.add(student_record)
    db.session.commit()
    return "jsonify(student_record.json)"


@app.route("/create")
def makeItSo():
    loadFromCSV()
    return "For 10 points, this mathematition invented taxicab numbers."


def loadFromCSV():

    students = []
    currentStudents = open("current_students.csv", "r")
    currentStudentsStringArray = currentStudents.read().split("\n")

    for string in currentStudentsStringArray:
        students.append(studentFromString(string))



    currentStudents.close()


def exportToCSV(students):

    now = datetime.datetime.now()
    fileName = str(now.year) + "_" + str(now.month) + "_" + str(now.day)
    output = open(fileName + ".csv", "w")

    for student in students:
        output.write(studentToString(student) + "\n")

    output.close()


if __name__ == "__main__":
    app.run()
    IPython.embed()
