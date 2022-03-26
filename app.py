from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from functions import update_pomodoro
from datetime import datetime, date
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    credit = db.Column(db.Integer)
    deadline = db.Column(db.DateTime)
    color = db.Column(db.String(7))
    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/')
def hello_world():
    '''new_subject = Subjects(name='Élettan',kredit=12,T=54)
    db.session.add(new_subject)
    db.session.commit()'''
    querys = Subjects.query.all()
    mylist = []
    for query in querys:
        temp = []
        temp.append(query.name)
        temp.append(query.color)
        T = (datetime.date(query.deadline)-datetime.date(query.date_created)).days
        dt = round(update_pomodoro(T,query.credit * 14))
        diff = (datetime.date(datetime.now())- datetime.date(query.date_created)).days
        if diff % dt == 0:
            temp.append(int(diff / dt + 1))
        else:
            temp.append(int((diff - (diff % dt))/dt + 1))
        mylist.append(temp)


    
    return render_template('index.html',subjects=mylist)


@app.route('/addtask',methods=['GET','POST'])
def add_task():
    if request.method == 'POST':
        name = request.form['subjectName']
        deadline = request.form['subjectDeadline'].split('-')
        credits = request.form['subjectCredits']
        color = request.form['subjectColor']
        new_subject = Subjects(name=name,credit=credits,deadline=datetime(int(deadline[0]),int(deadline[1]),int(deadline[2])),color=color)
        db.session.add(new_subject)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('addtask.html')



if __name__ == '__main__':
    app.run(debug=True)
