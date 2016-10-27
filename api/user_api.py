from flask import *
from extensions import *
from config import *
import hashlib
import uuid
import os
import re

user_api = Blueprint('user_api', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')



@user_api.route('/api/v1/user', methods=['GET', 'POST', 'PUT'])
def user_route():

	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']
	json_error = {}


#GET REQUEST OPTION
	if request.method == 'GET':
		print "are we checking 1"
		if 'username' in session:
			current_username = session['username']
			cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
			query = cur.fetchall()
			current_firstname = query[0]['firstname']
			current_lastname = query[0]['lastname']
			current_email = query[0]['email']
			print "returning json object after check"
			return jsonify(username=current_username,firstname=current_firstname, lastname=current_lastname, email=current_email)
		else:
			print "are we checking 2"
			json_error = {
				"errors":[
						{
							"message": "You do not have the necessary credentials for the resource"
    					}
    				]
    			}
    			print "returning json error after check"
    		return jsonify(json_error), 401







#POST REQUEST OPTION
	elif request.method == 'POST':

		error = False

		print "pre json input"

		user_input = request.get_json()
		print "user_input"
		print user_input
		print request

		print "pre json input 2"

		field_error = False

		print "pre json input 3"

		if 'username' not in user_input:
			print "username error"
			field_error = True


		print "pre json input 4"

		if 'firstname' not in user_input:
			print "firstname error"
			field_error = True

		print "pre json input 5"

		if 'lastname' not in user_input:
			print "lastname error"
			field_error = True

		print "pre json input 6"

		if 'password1' not in user_input:
			print "password1 error"
			field_error = True

		if 'password2' not in user_input:
			print "password2 error"
			field_error = True

		print "pre json input 7"
		print "pre json input 3"

		#if 'password2' not in user_input:
			#print "password2 error"
			#field_error = True

		print "field error"
		print field_error

		if field_error == True:
			print "inside field error true"
			json_error = {"errors":[{"message": "You did not provide the necessary fields"}]}
			return jsonify(json_error), 422


		username = user_input['username']
		firstname = user_input['firstname']
		lastname = user_input['lastname']
		password1 = user_input['password1']
		password2 = user_input['password2']
		email = user_input['email']
		
		print "post json input"
		errors = []
		

		print "error checking 1"
		cur.execute("SELECT username from user")
		users = cur.fetchall()
		for sql_username in users:
			sql_username = sql_username['username']
			if username.lower() == sql_username.lower():
				errors.append({"message": "This username is taken"})
				error = True

		if len(username) < 3:
			errors.append({"message": "Usernames must be at least 3 characters long"})
			error = True
		if not re.match("^[\w\d_]*$", password1):
			errors.append({"message": "Usernames may only contain letters, digits, and underscores"})
			error = True
		if len(password1) < 8:
			errors.append({"message": "Passwords must be at least 8 characters long"})
			error = True
		if not re.match("^(?=.*[a-zA-z])(?=.*\d)", password1):
			errors.append({"message": "Passwords must contain at least one letter and one number"})
			error = True
		if not re.match("^[\w\d_]*$", username):
			errors.append({"message": "Passwords may only contain letters, digits, and underscores"})
			error = True
		if len(email) > 40:
			errors.append({"message": "Email must be no longer than 40 characters"})
			error = True

		#if len(username) == 0:
		#	username_blank = True
		#	error = True
		#if len(firstname) == 0:
		#	firstname_blank = True
		#	error = True
		#if len(lastname) == 0:
		#	lastname_blank = True
		#	error = True
		#if len(password1) == 0:
		#	password1_blank = True
		#	error = True
		#if len(email) == 0:
		#	email_blank = True
		#	error = True


		if len(username) > 20:
			errors.append({"message": "Username must be no longer than 20 characters"})
			error = True
		if len(firstname) > 20:
			errors.append({"message": "Firstname must be no longer than 20 characters"})
			error = True
		if len(lastname) > 20:
			errors.append({"message": "Lastname must be no longer than 20 characters"})
			error = True

		if password1 != password2:
			errors.append({"message:" "Passwords do not match"})
			error = True

		#handle an invalid email address
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			errors.append({"message": "Email address must be valid"})
			error = True


		if not error:
			print "NO ERRORS!"
			#create hashed password:
			algorithm = 'sha512'     
			password = password1   
			salt = uuid.uuid4().hex 

			m = hashlib.new(algorithm)
			m.update(salt + password)
			password_hash = m.hexdigest()

			final_password = "$".join([algorithm,salt,password_hash])

			print "inserting into sql"
			cur.execute("INSERT INTO user (username, firstname, lastname, password, email) VALUES (%s, %s, %s, %s, %s)", [username, firstname, lastname, final_password, email])
			
			print "returning jsonify object"
			return jsonify(username=username,firstname=firstname, lastname=lastname, password1=password1, password2=password2, email=email), 201



		json_error = {"errors": errors}
		print json_error
		return jsonify(json_error), 422



	#PUT REQUEST OPTION
	if request.method == 'PUT':
		print "put path"
		user_input = request.get_json()
		page_firstname = ""
		page_lastname = ""
		password = ""
		password1 = ""


		field_error = False

		if 'firstname' not in user_input:
			print "firstname error"
			field_error = True

		if 'lastname' not in user_input:
			print "lastname error"
			field_error = True

		if 'email' not in user_input:
			print "email error"
			field_error = True

		if 'password1' not in user_input:
			print "password1 error"
			field_error = True

		if 'password2' not in user_input:
			print "password2 error"
			field_error = True

		if field_error == True:
			print "inside field error true"
			json_error = {"errors":[{"message": "You did not provide the necessary fields"}]}
			return jsonify(json_error), 422


		print "no errors continuing"
		if 'username' in session:
			logged_in = True
			current_username = session['username']
		else:
			json_error = {
				"errors":[
						{
							"message": "You do not have the necessary credentials for the resource"
						}
					]
				}
			return jsonify(json_error), 401


		#print "fetching username"
		#email = user_input['email']
		#cur.execute("SELECT username FROM user WHERE email = %s",[email])
		#query = cur.fetchall()
		#username = query[0]['username']

		#error = False
		#errors = []


		#if username != current_username:
		#	json_error = {
		#		"errors":[
		#				{
		#					"message": "You do not have the necessary permissions for the resource"
		#				}
		#			]
		#		}
		#	return jsonify(json_error), 403


		if user_input['firstname']:
			firstname = user_input['firstname']
			if len(firstname) > 20:
				errors.append({"message": "Firstname must be no longer than 20 characters"})
				error = True

		if user_input['lastname']:
			lastname = user_input['lastname']
			if len(lastname) > 20:
				errors.append({"message": "Lastname must be no longer than 20 characters"})
				error = True

		if user_input['password1']:
			password1 = user_input['password1']
			if (len(password1) != 0) and (len(password2) != 0):
				if len(password1) < 8:
					errors.append({"message": "Passwords must be at least 8 characters long"})
					error = True
				if password1 != password2:
					errors.append({"message": "Passwords do not match"})
					error = True
				if not re.match("^(?=.*[a-zA-z])(?=.*\d)", password1):
					errors.append({"message": "Passwords must contain at least one letter and one number"})
					error = True
				if not re.match("^[\w\d_]*$", password1):
					errors.append({"message": "Passwords may only contain letters, digits, and underscores"})
					error = True
				if not re.match("^[\w\d_]*$", username):
					errors.append({"message": "Usernames may only contain letters, digits, and underscores"})
					error = True


		if user_input['email']:
			email = user_input['email']
			if len(email) > 40:
				errors.append({"message": "Email must be no longer than 40 characters"})
				error = True
			if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
				errors.append({"message": "Email address must be valid"})
				error = True



		if not error:
			#create hashed password:
			print "ARE WE HEREEE?????"
			algorithm = 'sha512'     
			password = password1   
			salt = uuid.uuid4().hex 

			m = hashlib.new(algorithm)
			m.update(salt + password)
			password_hash = m.hexdigest()

			final_password = "$".join([algorithm,salt,password_hash])

			if user_input['firstname']:
				print "update username"
				cur.execute("UPDATE user SET firstname = %s WHERE username = %s", [firstname, current_username])
			if user_input['lastname']:
				print "update lastname"
				cur.execute("UPDATE user SET lastname = %s WHERE username = %s", [lastname, current_username])
			if user_input['password1']:
				print "update firstname"
				cur.execute("UPDATE user SET password = %s WHERE username = %s", [final_password, current_username])
			if user_input['email']:
				print "update email"
				cur.execute("UPDATE user SET email = %s WHERE username = %s", [email, current_username])


			return jsonify(username=current_username,firstname=firstname, lastname=lastname, password1=password1, password2=password2, email=email), 201


		json_error = {
				"errors": errors 
				}
		return jsonify(json_error), 422







