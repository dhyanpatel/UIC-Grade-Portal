from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for
from lib.get_overall_grades import populate
import json

app = Flask(__name__)

# Database stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://asgupert:ghLl1r3FnTG7qgPfntIb3qWbm8bsHiDF@tantor.db.elephantsql.com:5432/asgupert'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(10))
    grades = db.Column(db.JSON)

    def __init__(self, hash, grades):
        self.hash = hash
        self.grades = grades

    def __repr__(self):
        return '<Student {0}>'.format(self.hash)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<student_code>')
def profile(student_code):
    user = User.query.filter_by(hash = student_code).first()
    return render_template('profile.html' , student_code = student_code, user = user)


@app.route('/post_student', methods = ['POST'])
def post_student():
    student_code = request.form['student_code']
    return redirect(url_for('profile', student_code = student_code))
    # return render_template("profile.html", student_code = student_code)


@app.route('/instructor_portal')
def instructor_portal():
    return render_template('instructor_entry.html')


@app.route('/post_instructor', methods = ['POST'])
def post_instructor():
    """Updates the database. Won't work for Initial Population
    Commented line will work for Initial Population"""
    grades = json.loads(populate())
    for student in grades:
        # sqlStudent = User(student, grades[student])
        sqlStudent = User.query.filter_by(hash = student).first().update(grades[student])
        db.session.add(sqlStudent)
        db.session.commit()
    return "Grades Updated. Success!"


if __name__ == '__main__':
    app.run()
