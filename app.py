from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

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


@app.route('/position')
def position():
    return render_template("position.html")


if __name__ == '__main__':
    app.run()
