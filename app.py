from flask import Flask, render_template, flash, request, session, redirect
from datetime import datetime
from DB.db_Manager import DBManager
from user_agents import parse

app = Flask(__name__)
app.config.from_pyfile('script.py')

app.secret_key = 'thisIsMySpecialSecret!'

DB = DBManager()


@app.route('/')
def home():

    session.pop('id', None)
    session.pop('group', None)
    session.pop('consent', None)
    session.pop('instructions', None)
    session.pop('disagree', None)
    session.pop('position', None)
    session.pop('info', None)
    session.pop('consent', None)
    session.pop('argumentsA', None)
    session.pop('argumentsB', None)
    session.pop('argumentsC', None)
    session.pop('argumentsD', None)
    session.pop('opinion', None)
    session.pop('demo1', None)
    session.pop('demo2', None)
    session.pop('last', None)

    user = request.headers.get('User-Agent')
    # user_agent = parse(user)

    # print("This is -> ", user_agent.is_pc)
    start = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    print(start)
    print("This is my SuperMAN -> " + user)
    print("This is my SuperMAN platform -> " + request.user_agent.platform)
    return render_template("final_project.html")


@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/errorHandle')
def errorHandle():
    if session['consent'] == 1 and session['instructions'] == 0:
        return redirect('/instructions')
    elif session['instructions'] == 1 and session['position'] == 0:
        return redirect('/position')
    elif session['position'] == 1 and session['info'] == 0:
        return redirect('/info')
    elif session['info'] == 1 and session['argumentsA'] == 0 and session['argumentsB'] == 0 and \
            session['argumentsC'] == 0 and session['argumentsD'] == 0:
        if session['group'] == 1:
            return redirect('/1')
        elif session['group'] == 2:
            return redirect('/2')
        elif session['group'] == 3:
            return redirect('/3')
        else:
            return redirect('/4')
    elif session['opinion'] == 0 and (session['argumentsA'] == 1 or session['argumentsB'] == 1 or \
            session['argumentsC'] == 1 or session['argumentsD'] == 1):
        return redirect('/opinion')
    elif session['opinion'] == 1 and session['demographic1'] == 0:
        return redirect('/demographic1')
    elif session['demographic1'] == 1 and session['demographic2'] == 0:
        return redirect('/demographic2')
    elif session['demographic2'] == 1 and session['last_page'] == 0:
        return redirect('/last_page')
    # elif session['consent'] == 1 and session['disagree'] == 0:
    #     return redirect('/consent')
    return redirect('/')


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/Check',methods= ['POST'])
def Check():
    agree=request.form['consent']
    if agree == 'agree':
        session['consent'] = 1
        return redirect('/instructions')
    return redirect('/disagree')


@app.route('/disagree')
def disagree():

    session['consent'] = 1
    return render_template("disagree.html")


@app.route('/instructions')
def instructions():
    return render_template("instructions.html")


@app.route('/position')
def position():
    session['instructions'] = 1
    return render_template("position.html")


@app.route('/info')
def info():
    session['position'] = 1
    return render_template("info.html")


@app.route('/1')
def arguments1():
    session['info'] = 1
    return render_template("argumentsA.html")


@app.route('/2')
def arguments2():
    session['info'] = 1
    return render_template("argumentsB.html")


@app.route('/3')
def arguments3():
    session['info'] = 1
    return render_template("argumentsC.html")


@app.route('/4')
def arguments4():
    session['info'] = 1
    return render_template("argumentsD.html")


@app.route('/opinion')
def opinion():
    session['argumentsA'] = 1
    session['argumentsB'] = 1
    session['argumentsC'] = 1
    session['argumentsD'] = 1
    return render_template("opinion.html")


@app.route('/demographic1')
def demographic1():
    session['opinion'] = 1
    return render_template("demographic1.html")


@app.route('/demographic2')
def demographic2():
    session['demographic1'] = 1
    return render_template("demographic2.html")




@app.route('/connect',methods= ['POST'])
def connect():
    entryCode = request.form['entryCode']
    num = DB.getFromCodes(entryCode)
    print(num)

    if num == False:
        flash('The entry code is wrong, please try again')
        return redirect('/')
    deviceDB = num[0][3]
    user = request.headers.get('User-Agent')
    is_pc = parse(user).is_pc
    if is_pc == True:
        entryDevice = 1
    else:
        entryDevice = 0

    group = num[0][1]

    if num[0][2] == 1:
        finish = True
    else:
        finish = False

    if finish == False:
        if deviceDB == entryDevice:
            session['id'] = entryCode
            session['group'] = group
            session['consent'] = 0
            session['instructions'] = 0
            session['disagree'] = 0
            session['position'] = 0
            session['info'] = 0
            session['argumentsA'] = 0
            session['argumentsB'] = 0
            session['argumentsC'] = 0
            session['argumentsD'] = 0
            session['opinion'] = 0
            session['demo1'] = 0
            session['demo2'] = 0
            session['last'] = 0
            session['page'] = 'page'
            return redirect('/consent')
        else:
            flash('Please enter from the device you were asked in the instructions')
            return redirect('/')
    else:
        flash('you already finished your task, thank you!')
        return redirect('/')

@app.route('/handlePostions',methods= ['POST'])
def handleposition():
    s1 = request.form['s1']
    s2 = request.form['s2']
    s3 = request.form['s3']
    s4 = request.form['s4']
    s5 = request.form['s5']
    s6 = request.form['s6']
    print(s1)
    if s1 == '-1' or  s2 == '-1' or s3 == '-1' or s4 == '-1' or s5 == '-1' or s6 == '-1':
        print('Im in the if')
        flash("Please mark your level of agreement for all the statement")
        return redirect('/position')
    else:
        DB.insertPosition( session['id'], s1, s2, s3, s4, s5, s6)
        return redirect('/info')


@app.route('/handleOpinion',methods= ['POST'])
def handleOpinion():
    o1 = request.form['o1']
    o4 = request.form['o4']
    print(o1)
    if o1 == '-1' or o4 == '-1':
        print('Im in the if')
        flash("Please mark your level of agreement for all the statement")
        return redirect('/opinion')
    else:
        DB.insertOpinion( session['id'], o1, o4)
        return redirect('/demographic1')


@app.route('/handleDemo1',methods= ['POST'])
def handleDemo1():
    age = request.form['age']
    gender = request.form['gender']
    education = request.form['education']
    income = request.form['income']
    employment = request.form['employment']
    computer = request.form['computer']
    phone = request.form['phone']
    print(age)
    DB.insertDemo1(session['id'], age, gender,education, income,employment,computer, phone)
    return redirect('/demographic2')


@app.route('/handleDemo2', methods=['POST'])
def handleDemo2():
    myspace = request.form['myspace']
    space_scale = request.form['space_scale']
    space_private = request.form['space_private']
    space_size = request.form['space_size']
    noise = request.form['noise']
    dark = request.form['dark']
    density = request.form['density']
    DB.insertDemo2(session['id'], myspace, space_scale,space_private, space_size, noise, dark, density)
    return redirect('/last_page')

@app.route('/last_page')
def last_page():
    session['demographic2'] = 1
    end_time = datetime.now().strftime("%H:%M:%S")
    DB.updateCodes(session['id'], end_time)
    session.pop('id', None)
    return render_template("last_page.html")


if __name__ == '__main__':
    app.run()
