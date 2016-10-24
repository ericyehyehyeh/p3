from flask import *
from extensions import *
from config import *
import os

albums = Blueprint('albums', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p2')

@albums.route('/albums/edit', methods = ['GET', 'POST'])
def albums_edit_route():

	print "EDIT VIEW"

	method = request.form.get('op')

	logged_in = False
	if 'username' in session:
		logged_in = True
		current_username = session['username']


	db = connect_to_database()
	cur = db.cursor()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()

	cur.execute("SELECT username FROM user WHERE username = %s" , [current_username])
	invalidUser = cur.fetchall()
	if not bool(invalidUser):
		abort(404)
	
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
			print "picid"
			print picid

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

	print "ALBUMS VIEW"
	users_page = request.args.get('username')

	db = connect_to_database()
	cur = db.cursor()

	logged_in = False
	if 'username' in session:
		logged_in = True
		current_username = session['username']

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

	public = False

	if (logged_in == False):
		cur.execute("SELECT access FROM album where username = %s", [users_page])
		albums_access = cur.fetchall()
		for access in albums_access:
			access = access['access']
			if access == "public":
				public = True

	if (public == False) & (logged_in == False):
		return redirect("/gu4wdnfe/p2/")


	options = {
		"results": results,
		"logged_in": logged_in,
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




