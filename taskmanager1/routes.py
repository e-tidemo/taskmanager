from flask import render_template
from taskmanager1 import app, db


@app.route("/")
def home():
    return render_template("tasks.html")