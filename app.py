from flask import Flask, render_template, flash, request, session,url_for, redirect
from DB.db_Manager import DBManager

app = Flask(__name__)
app.config.from_pyfile('script.py')

app.secret_key = 'thisIsMySpecialSecret!'

DB = DBManager()


@app.route('/')
def home():
    user = request.headers.get('User-Agent')
    print("This is my SuperMAN -> " + user)
    print("This is my SuperMAN platform -> " + request.user_agent.platform)
    return render_template("final_project.html")


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/disagree')
def disagree():
    return render_template("disagree.html")



@app.route('/Check',methods= ['POST'])
def Check():
    agree=request.form['consent']
    if agree=='agree':
        return render_template("instructions.html")
    return render_template("disagree.html")


@app.route('/demographic1')
def demographic1():
    return render_template("demographic1.html")

@app.route('/demographic2')
def demographic2():
    return render_template("demographic2.html")


@app.route('/instructions')
def instructions():
    return render_template("instructions.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/1')
def arguments1():
    return render_template("argumentsA.html")


@app.route('/2')
def arguments2():
    return render_template("argumentsB.html")


@app.route('/3')
def arguments3():
    return render_template("argumentsC.html")


@app.route('/4')
def arguments4():
    return render_template("argumentsD.html")


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
    getEntryCode=DB.getEntryCode(entryCode)

    if not getEntryCode:
        flash('The entry code is wrong, please try again')
        return redirect('/')
    finish = DB.getfinish(entryCode)
    if finish:
        session['id'] = entryCode
        session['group'] = group
        return redirect('/consent')
    else:
        flash('you already finished your task, thank you!')
        return redirect('/')


if __name__ == '__main__':
    app.run()
