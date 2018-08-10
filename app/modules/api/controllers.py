from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from flask_jwt_extended import (
    jwt_required, get_jwt_identity, get_jwt_claims, get_current_user
)
from sqlalchemy import inspect

from app.modules.models import User, db

mod_api = Blueprint('api', __name__, url_prefix='/api', template_folder='templates')

@mod_api.route('/sample')
@jwt_required
def sample():
    print get_jwt_claims()
    return "asdasd", 200

@mod_api.route('/profile', methods=['POST', 'PUT'])
@jwt_required
def profile():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    if request.method == 'PUT':
        identity = get_jwt_claims()
        mapper = inspect(User)
        try:
            rows_changed = User.query.filter_by(id=identity['id']).update(request.json)
            db.session.commit()
            return jsonify(msg='User successfully updated'), 200
        except AssertionError as exception_message:
            return jsonify(msg='Error: {}. '.format(exception_message)), 400
