from flask import Blueprint, render_template, request, redirect, url_for
# import firebase_admin
# from firebase_admin import auth

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # Firebase login logic
    return redirect(url_for('main.index'))

@main.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    # Firebase signup logic
    return redirect(url_for('main.index'))
