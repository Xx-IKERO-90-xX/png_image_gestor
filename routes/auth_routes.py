import os
import sys
from flask import request, Flask, render_template, redirect, session, sessions, url_for, Blueprint
from extensions import db

auth_bp = Blueprint('auth', __name__)
