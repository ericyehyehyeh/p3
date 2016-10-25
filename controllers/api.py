from flask import *
from extensions import *
from config import *
import os

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')


@api.route('/api/v1/login', methods=['POST'])
def login_route():
	print "login_route achieved"
	#dealWithPostData(request.get_json());
	username = request.form['username'];
	#username = "test"
	print "username inputted: " + username;
	password = request.form['password'];
	print "password inputted: " + password;



	#check if valid function
	#errorType = "invalid username";
	if True:
		return jsonify(username=username,password=password)
	else:
		return jsonify({'error': errorType})