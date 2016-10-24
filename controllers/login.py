from flask import *
from extensions import *
from config import *
import hashlib
import uuid



login = Blueprint('login', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p2')

@login.route('/login', methods = ['GET','POST'])
def login_route():

	db = connect_to_database()
	cur = db.cursor()
	
	nonexistent_username = False
	nonexistent_password = False
	no_username = False
	no_password = False

	entered_user = ""
	entered_pass = ""
	post_requested = False

	if request.method == "POST":
		post_requested = True
		username = request.form.get('username')
		password = request.form.get('password')
		entered_user = username
		entered_pass = password
		failed = False
		

		
		cur.execute('SELECT password FROM user WHERE username = %s', [username])
		usernameResult = cur.fetchall()
	

		redirectToHome = False	

		if not bool(usernameResult):
			failed = True
			#errorMessage = "Username does not exist"
			nonexistent_username = True
		else:
			failed = True
			sqlPassword = usernameResult[0]['password']

			mytuple = sqlPassword.rsplit('$',2)

			#failed = True
			#errorMessage = "Real Pass: " + sqlPassword

			algorithm = mytuple[0]    
			salt = mytuple[1] 
			m = hashlib.new(algorithm)
			m.update(salt + password)
			password_hash = m.hexdigest()
			final_password = "$".join([algorithm,salt,password_hash])

			if final_password == sqlPassword:
				session['username'] = username
				return redirect("/gu4wdnfe/p2/")
			else:
				#errorMessage = "Password is incorrect for the specified username"
				nonexistent_password = True
				failed = True
			#if passwords are equal, start session, otherwise change error message
			#redirect to home = true
	else:
		failed = False
		#errorMessage = ""
		redirectToHome = False

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()

	username_empty = False
	
	if post_requested == True and entered_user == "":
		username_empty = True
		nonexistent_username = False
		no_username = True
		#errorMessage = ""
		#errorMessage += "Username may not be left blank"

	if post_requested == True and entered_pass == "":
		nonexistent_username = False
		nonexistent_password = False
		no_password = True		
		
	options = {
		"failed": failed,
		#"errorMessage": errorMessage,
		"pub_user_albums": pubalbums,
		"results": results,
		"nonexistent_username": nonexistent_username,
		"nonexistent_password": nonexistent_password,
		"no_username": no_username,
		"no_password":  no_password
	}
	
	if redirectToHome:
		return redirect("/gu4wdnfe/p2/")
	else:
		return render_template("login.html", **options)

