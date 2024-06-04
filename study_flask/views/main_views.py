from flask import Blueprint, url_for
from werkzeug.utils import redirect
from ..models.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_flask():
	return '어서와 플라스크는 처음이지!'

@bp.route('/')
def index():
	return redirect(url_for('question._list'))
