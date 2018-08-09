from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_jwt_extended import (
    jwt_required, get_jwt_identity, get_jwt_claims
)

mod_api = Blueprint('api', __name__, url_prefix='/api', template_folder='templates')

@mod_api.route('/sample')
@jwt_required
def sample():
    print get_jwt_claims()
    return "asdasd", 200
