from flask import Flask
# from firebase_admin import credentials, initialize_app
import json

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    cred = credentials.Certificate(json.loads(app.config['FIREBASE_CREDENTIALS']))
    initialize_app(cred)

    #Change 1
    #Change 2

    from .routes import main
    app.register_blueprint(main)

    return app
