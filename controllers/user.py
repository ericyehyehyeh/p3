from flask import *
from extensions import *
from config import *
import hashlib
import uuid
import re
import os




user = Blueprint('user', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p2')


@user.route('/user', methods = ['GET','POST'])
def user_route():



	if 'username' in session:
		logged_in = True
		return redirect("/gu4wdnfe/p2/user/edit")


	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']


	errorMessage = ""

	username_blank = False
	firstname_blank = False
	lastname_blank = False
	password1_blank = False
	email_blank = False
	username_long = False
	firstname_long = False
	lastname_long = False
	username_not_unique = False
	username_short = False
	password_short = False
	password_mismatch = False
	email_long = False
	email_invalid = False
	username_characters = False
	password1_characters = False
	password1_invalid = False
	error = False


	username = request.form.get('username')
	if username is None:
			username = ''

	firstname = request.form.get('firstname')
	if firstname is None:
			firstname = ''

	lastname = request.form.get('lastname')
	if lastname is None:
			lastname = ''

	password1 = request.form.get('password1')
	if password1 is None:
			password1 = ''

	password2 = request.form.get('password2')
	if password2 is None:
			password2 = ''

	email = request.form.get('email')
	if email is None:
			email = ''

	
	#error checking:
	if request.method == "POST":


		cur.execute("SELECT username from user")
		users = cur.fetchall()
		for sql_username in users:
			sql_username = sql_username['username']
			print "sql username", sql_username
			if username.lower() == sql_username.lower():
				username_not_unique = True
				error = True


		if re.match("^(?=.*[a-zA-z])(?=.*\d)", username):
			username_characters = True
			error = True

		if re.match("^[\w\d_]*$", password1):
			password1_characters = True
			error = True

		if re.match("^(?=.*[a-zA-z])(?=.*\d)", password1):
			password1_invalid = True
			error = True

		if len(username) < 3:
			username_short = True
			error = True

		if len(password1) < 8:
			password_short = True
			error = True


		if len(email) > 40:
			email_long = True
			error = True

		if len(username) == 0:
			username_blank = True
			error = True
		if len(firstname) == 0:
			firstname_blank = True
			error = True
		if len(lastname) == 0:
			lastname_blank = True
			error = True
		if len(password1) == 0:
			password1_blank = True
			error = True
		if len(email) == 0:
			email_blank = True
			error = True


		if len(username) > 20:
			username_long = True
			error = True
		if len(firstname) > 20:
			firstname_long = True
			error = True
		if len(lastname) > 20:
			lastname_long = True
			error = True

		if password1 != password2:
			password_mismatch = True
			error = True

		#handle an invalid email address
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			email_invalid = True
			error = True

	


		if not error:
			#create hashed password:
			algorithm = 'sha512'     
			password = password1   
			salt = uuid.uuid4().hex 

			m = hashlib.new(algorithm)
			m.update(salt + password)
			password_hash = m.hexdigest()

			final_password = "$".join([algorithm,salt,password_hash])

			cur.execute("INSERT INTO user (username, firstname, lastname, password, email) VALUES (%s, %s, %s, %s, %s)", [username, firstname, lastname, final_password, email])

			return redirect("/gu4wdnfe/p2/login/")

	# if username_blank == False:
	# 	errorMessage += "username may not be left blank\n\n"
	# if firstname_blank == False:
	# 	errorMessage += "firstname may not be left blank\n\n"
	# if lastname_blank == False:
	# 	errorMessage += "lastname may not be left blank\n\n"
	# if password1_blank == False:
	# 	errorMessage += "password1 may not be left blank\n\n"
	# if email_blank == False:
	# 	errorMessage += "email may not be left blank\n\n"


	options = {
		"new_user": True,
		"edit_user": False,
		"username_blank": username_blank,
		"firstname_blank": firstname_blank,
		"lastname_blank": lastname_blank,
		"password1_blank": password1_blank,
		"email_blank": email_blank,
		"email_long": email_long,
		"username_long": username_long,
		"firstname_long": firstname_long,
		"lastname_long": lastname_long,
		"username_not_unique": username_not_unique,
		"username_short": username_short,
		"password_short": password_short,
		"password_mismatch": password_mismatch,
		"email_invalid": email_invalid,
		"username_characters": username_characters,
		"password1_characters": password1_characters,
		"password1_invalid": password1_invalid,
		"hostValue": host,
		"portValue": port
	}

	return render_template("user.html", **options)

@user.route('/user/edit', methods = ['GET','POST'])
def edit_user():

	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']

	if 'username' in session:
		logged_in = True
		current_username = session['username']
	else:
		return redirect("/gu4wdnfe/p2/user")

	firstname_long = False
	lastname_long = False
	password_short = False
	password_mismatch = False
	email_long = False
	email_invalid = False
	password1_characters = False
	password1_invalid = False
	error = False

	firstname = request.form.get('firstname')
	if firstname is None:
			firstname = ''

	lastname = request.form.get('lastname')
	if lastname is None:
			lastname = ''

	password1 = request.form.get('password1')
	if password1 is None:
			password1 = ''

	password2 = request.form.get('password2')
	if password2 is None:
			password2 = ''

	email = request.form.get('email')
	if email is None:
			email = ''


	#error checking:
	if request.method == "POST":
		field = request.form.get('field')

		if field == "firstname":
			print "where are we 3"
			if len(firstname) > 20:
				firstname_long = True
				error = True

		if field == "lasstname":
			print "where are we 4"
			if len(lastname) > 20:
				lastname_long = True
				error = True

		if field == "password":
			print "where are we 5"
			if len(password1) < 8:
				password_short = True
				error = True
			if password1 != password2:
				password_mismatch = True
				error = True
			if re.match("^[\w\d_]*$", password1):
				password1_characters = True
				error = True
			if re.match("^(?=.*[a-zA-z])(?=.*\d)", password1):
				password1_invalid = True
				error = True

		if field == "email":
			print "where are we 6"
			if len(email) > 40:
				email_long = True
				error = True
			if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
				email_invalid = True
				error = True



		if not error:
			print "where are we 7"
			#create hashed password:
			algorithm = 'sha512'     
			password = password1   
			salt = uuid.uuid4().hex 

			m = hashlib.new(algorithm)
			m.update(salt + password)
			password_hash = m.hexdigest()

			final_password = "$".join([algorithm,salt,password_hash])

			if field == "firstname":
				cur.execute("UPDATE user SET firstname = %s WHERE username = %s", [firstname, current_username])
			if field == "lastname":
				cur.execute("UPDATE user SET lastname = %s WHERE username = %s", [lastname, current_username])
			if field == "password":
				cur.execute("UPDATE user SET password = %s WHERE username = %s", [final_password, current_username])
			if field == "email":
				cur.execute("UPDATE user SET email = %s WHERE username = %s", [email, current_username])

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()


	options = {
		"new_user": False,
		"edit_user": True,
		"logged_in": logged_in,
		"firstname_long": firstname_long,
		"lastname_long": lastname_long,
		"password_short": password_short,
		"email_long": email_long,
		"password_mismatch": password_mismatch,
		"email_invalid": email_invalid,
		"password1_characters": password1_characters,
		"password1_invalid": password1_invalid,
		"pub_user_albums": pubalbums,
		"results": results,
		"hostValue": host,
		"portValue": port
	}


	return render_template("user.html", **options)


