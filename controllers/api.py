from flask import *
from extensions import *
from config import *
import os

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@api.route("/api/v1/user", methods=['GET','POST','PUT'])
def userApi():
	
	db = connect_to_database()
	cur = db.cursor()

	if request.method == "GET":
		if 'username' in session:
			current_username = session['username']
			cur.execute("SELECT * FROM user WHERE username = %s", [current_username])
			query = cur.fetchall()
			firstname = query[0]['firstname']
			lastname = query[0]['lastname']
			email = query[0]['email']

			userDict = {
				"username": current_username,
				"firstname": firstname,
				"lastname": lastname,
				"email": email
			}

			return jsonify(userDict)


	elif request.method == "POST":
		#have to insert error checking, is this dealt with within
		#the HTML error tags or here or javascript? Implementation
		#finished for no errors, most likely post error code

		username = request.form.get('username')
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		email = request.form.get('email')

		userDict = {

		}

		return jsonify(userDict)


	else:
		userDict = {

		}

		return jsonify(userDict)
		# deal with put request

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

@api.route('/api/v1/logout', methods=["POST"])
def logout_route():
	
	if request.method == "POST":
		print "Made it inside logout"
		#deal with post request

@api.route('/api/v1/album/<albumid>', methods=["GET"])
def album_route():
	
	if request.method == "GET":
		print "Made it inside album"
		#deal with get request
	
@api.route('/api/v1/pic/<picid>', methods=["GET","PUT"])
def pic_route():
	
	if request.method == "GET":
		print "Made it inside GET"
		#deal with get request
	
	elif request.method == "PUT":
		print "MAde it inside final PUT"
		#deal with put request
			
