from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for

app = Flask(__name__)

# Database stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/flasktesting'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_code = db.Column(db.String(10))
    Lab_Quiz1 = db.Column(db.String(80))
    Lab_Quiz2 = db.Column(db.String(80))
    Lab_Quiz3 = db.Column(db.String(80))
    Lab_Quiz4 = db.Column(db.String(80))
    Lab_Quiz5 = db.Column(db.String(80))
    Lab_Quiz6 = db.Column(db.String(80))
    Lab_Quiz7 = db.Column(db.String(80))
    Lab_Quiz8 = db.Column(db.String(80))
    Lab_Quiz9 = db.Column(db.String(80))
    program1_run = db.Column(db.String(80))
    program2_run = db.Column(db.String(80))
    program3_run = db.Column(db.String(80))
    program4_run = db.Column(db.String(80))
    program5_run = db.Column(db.String(80))
    program6_run = db.Column(db.String(80))
    program1_style = db.Column(db.String(80))
    program2_style = db.Column(db.String(80))
    program3_style = db.Column(db.String(80))
    program4_style = db.Column(db.String(80))
    program5_style = db.Column(db.String(80))
    program6_style = db.Column(db.String(80))

    def __init__(self, student_code,
                 Lab_Quiz1, Lab_Quiz2, Lab_Quiz3, Lab_Quiz4, Lab_Quiz5, Lab_Quiz6, Lab_Quiz7, Lab_Quiz8, Lab_Quiz9,
                 program1_run, program2_run, program3_run, program4_run, program5_run, program6_run,
                 program1_style, program2_style, program3_style, program4_style, program5_style, program6_style):
        self.student_code = student_code
        self.Lab_Quiz1 = Lab_Quiz1
        self.Lab_Quiz2 = Lab_Quiz2
        self.Lab_Quiz3 = Lab_Quiz3
        self.Lab_Quiz4 = Lab_Quiz4
        self.Lab_Quiz5 = Lab_Quiz5
        self.Lab_Quiz6 = Lab_Quiz6
        self.Lab_Quiz7 = Lab_Quiz7
        self.Lab_Quiz8 = Lab_Quiz8
        self.Lab_Quiz9 = Lab_Quiz9
        self.program1_run = program1_run
        self.program2_run = program2_run
        self.program3_run = program3_run
        self.program4_run = program4_run
        self.program5_run = program5_run
        self.program6_run = program6_run
        self.program1_style = program1_style
        self.program2_style = program2_style
        self.program3_style = program3_style
        self.program4_style = program4_style
        self.program5_style = program5_style
        self.program6_style = program6_style

    def __repr__(self):
        return '<Student %r>' % self.student_code


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<student_code>')
def profile(student_code):
    return render_template('profile.html' , student_code = student_code)


@app.route('/post_student', methods = ['POST'])
def post_student():
    student_code = request.form['student_code']
    return redirect(url_for('profile', student_code = student_code))
    # return render_template("profile.html", student_code = student_code)


if __name__ == '__main__':
    app.run()
