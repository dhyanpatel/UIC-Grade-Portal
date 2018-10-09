from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Database stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/flasktesting'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lab_Quiz1 = db.Column(db.String(80))
    lab_Quiz2 = db.Column(db.String(80))
    lab_Quiz3 = db.Column(db.String(80))
    lab_Quiz4 = db.Column(db.String(80))
    lab_Quiz5 = db.Column(db.String(80))
    lab_Quiz6 = db.Column(db.String(80))
    lab_Quiz7 = db.Column(db.String(80))
    lab_Quiz8 = db.Column(db.String(80))
    lab_Quiz9 = db.Column(db.String(80))
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

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<user_id>')
def profile(user_id):
    return  render_template('profile.html' , user_id = user_id)



if __name__ == '__main__':
    app.run()
