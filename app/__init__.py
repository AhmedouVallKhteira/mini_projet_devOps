from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '123451$#FTRFTGFGR#Yq2q212287'
    
    app.register_blueprint(main)

    return app
