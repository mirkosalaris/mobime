from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!", contacts=['c1', 'c2', 'c3', 'c4', 'c5'])
