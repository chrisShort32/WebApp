from flask import Flask, render_template
from waitress import serve
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breakfast/<item>')
def breakfast(item):
    return render_template('breakfast.html', item=item)

@app.route('/breakfast/<breakfast_choice>/breakfast_choice1')
def breakfast_choice1(breakfast_choice):
    return render_template('breakfast_choice1.html', breakfast_choice = breakfast_choice)

@app.route('/breakfast/<breakfast_choice>/breakfast_choice2')
def breakfast_choice2(breakfast_choice):
    return render_template('breakfast_choice2.html', breakfast_choice = breakfast_choice)

@app.route('/dinner/<item>')
def dinner(item):
    return render_template('dinner.html', item=item)


@app.route('/dinner/<dinner_choice>/dinner_choice1')
def dinner_choice1(dinner_choice):
    return render_template('dinner_choice1.html',dinner_choice = dinner_choice)


@app.route('/dinner/<dinner_choice>/dinner_choice2')
def dinner_choice2(dinner_choice):
    return render_template('dinner_choice2.html',dinner_choice = dinner_choice)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)