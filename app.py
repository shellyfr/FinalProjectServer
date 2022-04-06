from flask import Flask, render_template, flash, request, session,url_for, redirect
from DB.db_Manager import DBManager

app = Flask(__name__)
app.config.from_pyfile('script.py')

app.secret_key = 'thisIsMySpecialSecret!'

DB = DBManager()


@app.route('/')
def home():
    # session.pop('page', None)
    # session.pop('id', None)
    # # session.pop('group', None)
    # if session:
    #     if session['page']:
    #         if session['page'] != 1:
    #             return redirect('/consent')
    # session['page'] = 1
    # return render_template("final_project.html")
    user = request.headers.get('User-Agent')
    print("This is my SuperMAN -> " + user)
    print("This is my SuperMAN platform -> " + request.user_agent.platform)
    return render_template("final_project.html")


@app.route('/consent')
def consent():
    # if session['page'] == 1:
    #     session['page'] = 2
    #     return render_template("consent.html")
    # return redirect('/instructions')
        return render_template("consent.html")



@app.route('/Check',methods= ['POST'])
def Check():
    agree=request.form['consent']
    if agree=='agree':
        return redirect('/instructions')
    return redirect('/disagree')


@app.route('/disagree')
def disagree():
    session.pop('page', None)
    return render_template("disagree.html")


@app.route('/instructions')
def instructions():
    # if session['page'] == 2:
    #     session['page'] = 3
    #     return render_template("instructions.html")
    return redirect('/position')


@app.route('/position')
def position():
    # if session['page'] == 3:
    #     session['page'] = 4
    #     return render_template("position.html")
    # return redirect('/info')


    return render_template("position.html")


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


@app.route('/demographic1')
def demographic1():
    return render_template("demographic1.html")

@app.route('/demographic2')
def demographic2():
    return render_template("demographic2.html")


@app.route('/opinion')
def opinion():
    return render_template("opinion.html")


@app.route('/last_page')
def last_page():
    DB.updateCodes(session['id'])
    session.pop('id', None)
    return render_template("last_page.html")


@app.route('/connect',methods= ['POST'])
def connect():
    entryCode = request.form['entryCode']
    num = DB.getFromCodes(entryCode)
    deviceDB = num[0][3]
    OperatingSystem=request.user_agent.platform
    if OperatingSystem =="windows" or OperatingSystem =="macos" or OperatingSystem =="linux" :
        entryDevice=1
    elif OperatingSystem =='android' or OperatingSystem =='ios' or OperatingSystem =='blackberry OS' or OperatingSystem =='Windows OS' or OperatingSystem =='Symbian OS' or OperatingSystem =='Tizen':
        entryDevice=0

    if num == False:
        flash('The entry code is wrong, please try again')
        return redirect('/')
    group=num[0][1]

    if num[0][2] == 1:
        finish = True
    else:
        finish = False
    if finish == False:
        if deviceDB == entryDevice:
            print(OperatingSystem)
            session['id'] = entryCode
            session['group'] = group
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
    space = request.form['space']
    space_scale = request.form['space_scale']
    space_private = request.form['space_private']
    space_size = request.form['space_size']
    noise = request.form['noise']
    dark = request.form['dark']
    density = request.form['density']
    DB.insertDemo2(session['id'], space, space_scale,space_private, space_size, noise, dark, density)
    return redirect('/last_page')


if __name__ == '__main__':
    app.run()
