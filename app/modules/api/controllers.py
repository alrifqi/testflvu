from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_jwt_extended import jwt_required
from .models import User
from bson.json_util import dumps

mod_api = Blueprint('api', __name__, url_prefix='/api/v1', template_folder='templates')

@mod_api.route('/sample')
@jwt_required
def sample():
    results = User.get()
    res = dumps(results)
    return res, 200