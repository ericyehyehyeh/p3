from flask import *
from extensions import *
from config import *
import hashlib
import uuid
import os#possibly delete

login_api = Blueprint('login_api', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')


@login_api.route('/api/v1/login', methods=['POST'])
def login_api_route():

	data = request.get_json()
	username = data['username']
	password = data['password']

	if request.method == "":
		json_error = {
			"errors":[
						{
							"message": "You did not provide the necessary fields"
    					}
    				]
    			}
		return jsonify(error = json_error), 422
	
	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']

  	cur.execute("SELECT password FROM user WHERE username = %s", [username])
  	usernameResult = cur.fetchall()

	if not bool(usernameResult):
		json_error = {
			"errors":[
 						{
							"message": "Username does not exist"
    					}
  					]
				}
		return jsonify(error=json_error), 404

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
			session['username'] = username
			return jsonify(username=username, password=password)
		else:
			json_error = {
				"errors":[
 							{
								"message": "Password is incorrect for the specified username"
    						}
  						]
					}
			return jsonify(json_error), 422




