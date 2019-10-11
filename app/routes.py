from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!", contacts=['c1', 'c2', 'c3', 'c4', 'c5'])

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')
