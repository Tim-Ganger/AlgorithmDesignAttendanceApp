import datetime

from flask import Flask

app = Flask(__name__)


class Student():

    name = ""
    advisor = ""
    grade = 0
    parentEmail = ""
    status = ""

    def __init__(self, name, grade, advisor, parentEmail, status):
        self.name = name
        self.advisor = advisor
        self.grade = grade
        self.parentEmail = parentEmail
        self.status = status


def studentFromString(string):
    array = string.split(",")

    if array.length == 5:
        name = array[0]
        advisor = array[1]
        grade = int(array[2])
        parentEmail = array[3]
        status = array[4]
        return Student(name, advisor, grade, parentEmail, status)
    else:
        print("Not Propper String")


def studentToString(student):
    output = student.name + ", "
    output += student.advisor + ", "
    output += student.grade + ", "
    output += student.parentEmail + ", "
    output += student.status

    return output


@app.route("/")
def hello():
    # s = Student("EJ Eppinger", 12, "Nassar", "parentemail@email.com", "p")
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

    output = open(now.year + "_" + now.month + "_" + now.day + ".csv", "w")

    for student in students:
        output.write(studentToString(student) + "\n")

    output.close()


if __name__ == "__main__":

    app.run()
