import datetime
import IPython
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Basic setup for app with Flask and SQLAlchemy
laapp = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)


class Student(db.Model):
    """Class to hold information for Student."""

    # Initialize instance variables.
    __tablename__ = 'UserRemap'
    firstName = db.Column(db.String, primary_key=True)
    lastName = db.Column(db.String, primary_key=True)
    advisor = db.Column(db.String)
    grade = db.Column(db.String)
    parentEmail = db.Column(db.String)
    status = db.Column(db.String)
    lateTime = db.Column(db.Time)

    def __init__(self, first, last, grade, advisor, parentEmail, status):
        """Default constructor for Student class."""

        self.firstName = first
        self.lastName = last
        self.advisor = advisor
        self.grade = grade
        self.parentEmail = parentEmail
        self.status = status
        if status != "p" and lateTime is not None:
            self.lateTime = lateTime

        def __repr__(self):
            """Make student class print to console cleanly for testing."""

            name = self.firstName + " " + self.lastName
            return "Student Info: " + name + ", " + self.advisor


        @property
        def json(self):
            """Allow the json representation of the Student to be accessed as a
            property using .json"""

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
    output += student.advisor + ", "
    output += student.grade + ", "
    output += student.parentEmail + ", "
    output += student.status

    return output


def studentFromString(string):

    array = string.split(",")

    if len(array) == 4:
        first = array[0].strip()
        last = array[1].strip()
        grade = array[2].strip()
        advisor = array[3].strip()
        parentEmail = ""
        status = ""
        return Student(last, first, grade, advisor, parentEmail, status)

    if len(array) == 6:

        first = array[0].strip()
        last = array[1].strip()
        grade = array[2].strip()
        advisor = array[3].strip()
        parentEmail = array[4].strip()
        status = array[5].strip()
        return Student(first, last, advisor, grade, parentEmail, status)

    else:
        print("Not Propper String")


@app.route("/")
def hello():

    # s = Student("EJ", Eppinger", "12th Grade", "Nassar", "parentemail@email.com", "p")
    # print(s)
    return "Hello World!"


def loadFromCSV():

    students = []
    currentStudents = open("current_students.csv", "r")
    currentStudentsStringArray = currentStudents.read().split("\n")
    currentStudentsStringArray.remove(currentStudentsStringArray[0])
    # currentStudentsStringArray.remove("")
    currentStudents.close()

    for string in currentStudentsStringArray:
        students.append(studentFromString(string))

    return students


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
