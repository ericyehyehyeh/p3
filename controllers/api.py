from flask import *
from extensions import *
from config import *
import os

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@api.route('/testroute/<testvariable>')
def test_route(testvariable):
	return testvariable

@api.route('/api/v1/login')
def login_route():
	