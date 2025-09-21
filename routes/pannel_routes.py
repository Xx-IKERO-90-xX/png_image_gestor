import os
import sys
from flask import request, Flask, render_template, redirect, session, sessions, url_for, Blueprint
from extensions import db
from models.Image import Image
import json

pannel_bp = Blueprint('pannel', __name__)

settings = {}
with open("settings.json") as setting:
    settings = json.load(setting)

@pannel_bp.route('/', methods=['GET'])
async def index():
    if 'id' in session:
        page = request.args.get("page", 1, type=int)
        images = db.session.query(Image).paginate(page=page, per_page=5)

        ip = settings['flask']['ip']
        port = settings['flask']['port']
        
        return render_template(
            '/pannel/index.jinja',
            images=images,
            ip=ip,
            port=port,
            session=session
        )

    else:
        return redirect(url_for('index'))