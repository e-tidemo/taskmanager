from flask import render_template
from taskmanager1 import app, db


@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/add_category", method=["GET", "POST"])
def add_category():
    return render_template("add_category.html")