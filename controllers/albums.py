from flask import *
from extensions import *
from config import *
import os

albums = Blueprint('albums', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@albums.route('/albums/edit', methods = ['GET', 'POST'])
def albums_edit_route():


	method = request.form.get('op')
	db = connect_to_database()
	cur = db.cursor()
	logged_in = False
	firstname = ""
	lastname = ""
	if 'username' in session:
		logged_in = True
		current_username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']
	else:
		return redirect("/gu4wdnfe/p3/login")


	
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()

	
	host = env['host']
	port = env['port']


	if method == "add":
		title = request.form.get('title')
		#username = request.form.get('username')
		cur.execute("INSERT INTO album (title, username) VALUES (%s, %s)", [title, current_username])

	if method == "delete":
		albumid = request.form.get('albumid')
		cur.execute("SELECT picid FROM contain WHERE albumid = %s", [albumid])
		del_photos = cur.fetchall()


		for photo in del_photos:
			picid = photo['picid']

			cur.execute("SELECT format FROM photo WHERE picid = %s", [picid])

			new_pic_format = cur.fetchall()
			pic_format = new_pic_format[0]['format']

			cur.execute("DELETE FROM contain WHERE picid = %s", [picid])

			cur.execute("DELETE FROM photo WHERE picid = %s", [picid])

			os.remove(os.path.join('static/images/', picid + "." + pic_format))

		cur.execute("DELETE FROM AlbumAccess WHERE albumid = %s", [albumid])
		cur.execute("DELETE FROM album WHERE albumid = %s", [albumid])


	cur.execute("SELECT title, albumid FROM album WHERE username = %s" , [current_username])
	albums = cur.fetchall()


	options = {
		"edit": True,
		"not-edit": False,
		"firstname": firstname,
		"lastname": lastname,
		"results": results,
		"albums": albums,
		"user_name": current_username,
		"logged_in": logged_in,
		"private_view": True,
		"hostValue": host,
		"portValue": port,
		"pub_user_albums": pubalbums
	}


	return render_template("albums.html", **options)


@albums.route('/albums', methods=['GET', 'POST'])
def albums_route():

	users_page = request.args.get('username')

	db = connect_to_database()
	cur = db.cursor()

	logged_in = False
	firstname = ""
	lastname = ""
	if 'username' in session:
		logged_in = True
		current_username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']


	if users_page is not None:
		cur.execute("SELECT username FROM user WHERE username = %s" , [users_page])
		invalidUser = cur.fetchall()
		if not bool(invalidUser):
			abort(404)

	username = request.args.get('username')

	if username is None:
		cur.execute("SELECT * from album where username = %s", [current_username])
		albums = cur.fetchall()
		private_view = True;
		user_name = current_username
	else:
		cur.execute("SELECT * from album where username = %s and access = 'public'", [username])
		albums = cur.fetchall()
		private_view = False
		user_name = username

	
	#side navigation bar
	cur.execute("SELECT username FROM user")
	results = cur.fetchall()
	host = env['host']
	port = env['port']
	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()



	options = {
		"results": results,
		"logged_in": logged_in,
		"firstname": firstname,
		"lastname": lastname,
		"albums": albums,
		"user_name": user_name,
		"hostValue": host,
		"portValue": port,
		"not-edit": True,
		"private_view": private_view,
		"edit": False,
		"pub_user_albums": pubalbums
	}

	return render_template("albums.html", **options)




