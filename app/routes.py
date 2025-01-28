from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/<name>')
def sayHello(name):
    return f'Hello {name}'

@main.route('/<name>/bye')
def sayBay(name):
    return f"Bye {name}"
