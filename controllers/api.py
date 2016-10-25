from flask import *
from extensions import *
from config import *
import hashlib
import uuid
import os#possibly delete

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
	if username is None or password is None:
		return jsonify(error="You did not provide the necessary fields"),422

	entered_user = username
	entered_pass = password
	
	db = connect_to_database()
	cur = db.cursor()
	cur.execute('SELECT password FROM user WHERE username = %s', [username])
	usernameResult = cur.fetchall()

	if not bool(usernameResult):
		print "username doesnt exist"
		JSONError = {
						"errors":	[
 										{
											"message": "Username does not exist"
    									}
  									]
					}
		return jsonify(JSONError), 404
	else:
		sqlPassword = usernameResult[0]['password']
		mytuple = sqlPassword.rsplit('$',2)
		algorithm = mytuple[0]    
		salt = mytuple[1] 
		m = hashlib.new(algorithm)
		m.update(salt + password)
		password_hash = m.hexdigest()
		final_password = "$".join([algorithm,salt,password_hash])

		if final_password == sqlPassword:
			print "password is correct, logging in"
			session['username'] = username
			return jsonify(username=username,password=password)
		else:
			print "incorrect password"
			return jsonify(error="Password is incorrect for the specified username"),422

	return jsonify(error="Reached end of route")






