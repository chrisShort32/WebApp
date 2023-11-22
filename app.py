from flask import Flask, render_template
from waitress import serve
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breakfast/<choice>')
def breakfast(choice):
    return render_template('breakfast.html', choice = choice)

@app.route('/breakfast/<breakfast_choice>')
def breakfast_choice1(breakfast_choice):
    return render_template('breakfast_choice1.html', breakfast_choice = breakfast_choice)

@app.route('/breakfast/<breakfast_choice>')
def breakfast_choice2(breakfast_choice):
    return render_template('breakfast_choice2.html', breakfast_choice = breakfast_choice)

@app.route('/dinner/<choice>')
def dinner(choice):
    return render_template('dinner.html', choice=choice)


@app.route('/dinner/<dinner_choice>')
def dinner_choice1(dinner_choice):
    return render_template('dinner_choice1.html',dinner_choice = dinner_choice)


@app.route('/dinner/<dinner_choice>')
def dinner_choice2(dinner_choice):
    return render_template('dinner_choice2.html',dinner_choice = dinner_choice)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)