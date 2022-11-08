from project import app
from flask import Blueprint
from flask import render_template




home = Blueprint('home', __name__, template_folder='template')

# home_page
@home.route("/")
def home_page():
    return  render_template('index.html')
