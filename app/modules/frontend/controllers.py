from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

mod_fe = Blueprint('root', __name__, url_prefix='/', template_folder='templates')


@mod_fe.route('/', methods=['GET'])
def index():
    return render_template('frontend/index.html')
