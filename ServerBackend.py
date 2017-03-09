from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

URI = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)

class Student(db.Model):

    __tablename__ = 'UserRemap'
    name = db.Column(db.String, primary_key=True)
    advisor = db.Column(db.String)
    grade = db.Column(db.Integer)
    parentEmail = db.Column(db.String)

    def __init__(self, name, grade, advisor, parentEmail):
        self.name = name
        self.advisor = advisor
        self.grade = grade
        self.parentEmail = parentEmail

    def __repr__(self):
        return "Student Info: " + self.name + ", " + self.advisor

    @property
    def json(self):
        return {
            "name": self.name,
            "advisor": self.advisor,
            "grade": self.grade,
            "parentEmail": self.parentEmail
        }


@app.route("/")
def hello():
    s = Student("EJ Eppinger", 12, "Nassar", "parentemail@email.com")
    return s.__repr__()


if __name__ == "__main__":
    app.run()
