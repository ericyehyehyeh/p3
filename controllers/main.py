from flask import *
from extensions import *
from config import *
from flask import Flask, session, redirect, url_for, escape, request


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/gu4wdnfe/p2/')
def main_route():
	
	db = connect_to_database()
	cur = db.cursor()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()
	host = env['host']
	port = env['port']

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()

	logged_in = False
	username = ""
	firstname = ""
	lastname = ""
	priv_albums = []
	my_albums = []
	if 'username' in session:
		logged_in = True
		username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']
		cur.execute("SELECT * FROM album where username = %s and access = 'private'", [username])
		my_albums = cur.fetchall()
		cur.execute("SELECT * FROM AlbumAccess where username = %s", [username])
		album_ids = cur.fetchall()
		for album_id in album_ids:
			album_id = album_id['albumid']
			cur.execute("SELECT * FROM album where albumid = %s", [albumid])
			priv = cur.fetchall()
			priv_album = priv[0]
			priv_albums.append(priv_album)


	options = {
		"home": True,
		"results": results,
		"hostValue": host,
		"portValue": port,
		"pub_user_albums": pubalbums,
		"private_albums": priv_albums,
		"username": username,
		"logged_in": logged_in,
		"my_albums": my_albums,
		"firstname": firstname,
		"lastname": lastname
	}

  	return render_template("base.html", **options)