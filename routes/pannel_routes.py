import os
import sys
from flask import request, Flask, render_template, redirect, session, sessions, url_for, Blueprint
from extensions import db

pannel_bp = Blueprint('pannel', __name__)