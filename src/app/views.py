from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/view")
def view():
    return render_template("view.html")