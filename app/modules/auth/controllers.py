from flask import Blueprint, jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_claims)
from werkzeug.security import check_password_hash
from app.modules.models import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@mod_auth.route('', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"msg": "Username Not Found"}), 400

    res = check_password_hash(user.password, password)
    if res:
        access_token = create_access_token(identity=user)
        return jsonify(access_token= access_token), 200
    else:
        return jsonify({"msg": "Wrong Password"}), 400


