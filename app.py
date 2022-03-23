from flask import Flask, render_template, flash, request, session,url_for, redirect
from DB.db_Manager import DBManager


import script

app = Flask(__name__)
app.config.from_pyfile('script.py')

app.secret_key = '1234'

DB = DBManager()

@app.route('/')
def home():
    return render_template("final_project.html")


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/questions')
def ques():
    return render_template("questions.html")


@app.route('/instructions')
def instructions():
    return render_template("instructions.html")


@app.route('/arguments')
def arguments():
    return render_template("arguments.html")

@app.route('/opinion')
def opinion():
    return render_template("opinion.html")


@app.route('/position')
def position():
    return render_template("position.html")

@app.route('/last_page')
def last_page():
    DB.user_finish(session['id'])
    session.pop('id', None)
    return render_template("last_page.html")


@app.route('/connect',methods= ['POST'])
def connect():
    entryCode = request.form['entryCode']
    group=DB.getgroupnum(entryCode)

    finish = DB.getfinish(entryCode)
    if group == "":
        flash('The entry code is wrong, please try again')
        return redirect('/')
    elif finish:
        session['id'] = entryCode
        return redirect('/consent')
    else:
        flash('you already finished your task, thank you!')
        return redirect('/')


if __name__ == '__main__':
    app.run()
