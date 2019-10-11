import os

from flask import render_template, request, url_for, redirect, send_from_directory
from app.fake_login import login_user, logout_user

from app import app
from app.common import common_variables


@app.route("/")
def index():
    return render_template("index.html", **common_variables())


@app.route('/about')
def about():
    return render_template('about.html', **common_variables())


@app.route('/profile')
def profile():
    return render_template('profile.html', **common_variables())


@app.route("/login",  methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html", **common_variables())
    else:
        login_user()
        return redirect(url_for("index"))


@app.route("/logout",  methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)
