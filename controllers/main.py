#/usr/bin/python
from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='views')

@main.route('/hello')
def main_route():
	return render_template("index.html")

@main.route('/')
def personal_route():
	return render_template("static_website.html")
