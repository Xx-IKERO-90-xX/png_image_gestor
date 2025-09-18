import os
import sys
import json
from datetime import datetime
from flask import request, Flask, render_template, redirect, session, sessions, url_for
from werkzeug.utils import secure_filename
import asyncio
from extensions import db

settings = {}

with open("settings.json") as setting:
    settings = json.load(setting)

app = Flask(__name__)
app.secret_key = "a40ecfce592fd63c8fa2cda27d19e1dbc531e946"
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{settings['mysql']['user']}:{settings['mysql']['passwd']}@{settings['mysql']['host']}/{settings['mysql']['db']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from routes.auth_routes import auth_bp
from routes.pannel_routes import pannel_bp
from routes.images_routes import images_bp  

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(pannel_bp, url_prefix="/pannel")
app.register_blueprint(images_bp, url_prefix="/images")
app.app_context()

@app.route('/')
async def index():
    return render_template('index.jinja')

if __name__ == "__main__":
    app.run(
        host=settings['flask']['host'],
        port=settings['flask']['port'],
        debug=settings['flask']['debug']
    )