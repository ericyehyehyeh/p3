from flask import *
from extensions import *
from config import *
import os

import hashlib

album = Blueprint('album', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@album.route('/album/edit', methods=['GET', 'POST'])


def album_edit_route():
	UPLOAD_FOLDER = '/static/images'

	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'bmp', 'gif'])
	
	def allowed_file(filename):
		return '.' in filename and \
			filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

	albumid = request.args.get('albumid')
	method = request.form.get('op')
	db = connect_to_database()
	cur = db.cursor()


	logged_in = False

	current_username = ""

	firstname = ""
	lastname = ""

	if 'username' in session:
		logged_in = True
		current_username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']

	if current_username == "":
		logged_in = False

	if logged_in == False:
		abort(403)

		

	caption_on = False
	owner = ""
	album_access = 'private'


	host = env['host']
	port = env['port']
	

	cur.execute("SELECT * FROM album WHERE albumid = %s" , [albumid])
	invalidUser = cur.fetchall()
	if not bool(invalidUser):
		abort(404)


	cur.execute("SELECT username, access from album where albumid = %s", [albumid])
	allowed_access = cur.fetchall()
	album_access = allowed_access[0]['access']
	owner = allowed_access[0]['username']

	if (current_username != owner):
		abort(403)
	else:
		owner_rights = True


	if method == "access":
		tempmethod = request.form.get('access')
		if tempmethod == "private":
			cur.execute("UPDATE album SET access = 'private' WHERE albumid = %s",[albumid])
			cur.execute("UPDATE album SET lastupdated = current_timestamp WHERE albumid = %s",[albumid])

		if tempmethod == "public":
			cur.execute("UPDATE album SET access = 'public' WHERE albumid = %s",[albumid])
			cur.execute("DELETE FROM AlbumAccess WHERE albumid = %s",[albumid])
			cur.execute("UPDATE album SET lastupdated = current_timestamp WHERE albumid = %s",[albumid])



	cur.execute("SELECT albumid FROM album WHERE albumid = %s" , [albumid])
	invalidUser = cur.fetchall()
	if not bool(invalidUser):
		abort(404)

	cur.execute('SELECT username FROM user')
	results = cur.fetchall()

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()


	cur.execute("SELECT picid, sequencenum FROM contain WHERE albumid = %s" , [albumid])
	pics = cur.fetchall()
	pic_format = []
	all_captions = []
	my_caption = ""
	new_edit = []
	for pic in pics:
		cur.execute("SELECT picid, format, date FROM photo WHERE picid = %s" , [pic['picid']])
		edit = cur.fetchall()

		cur.execute("SELECT caption FROM contain WHERE picid = %s" , [pic['picid']])
		captions = cur.fetchall()
		my_caption = captions[0]['caption']

		edit[0]['caption'] = my_caption
		new_edit = edit[0]

		pic_format.append(new_edit)

	if my_caption is not None:
		caption_on = True
	if len(my_caption) == 0:
		caption_on = False

		

	cur.execute("SELECT title FROM album WHERE albumid = %s" , [albumid])
	title = cur.fetchall()
	title = title[0]['title']




	cur.execute("SELECT sequencenum FROM contain ORDER BY sequencenum DESC")
	sequencenum = cur.fetchall()
	sequencenum = sequencenum[0]['sequencenum']



	if method == "grant":
		usernameEntered = request.form.get('username')
		cur.execute("INSERT INTO AlbumAccess(albumid,username) VALUES (%s,%s)",[albumid,usernameEntered])

	if method == "revoke":
		usernameDeleted = request.form.get('username')
		cur.execute("DELETE FROM AlbumAccess WHERE username = %s", [usernameDeleted])


	if method == "add":
		albumid = request.form.get('albumid')
		fileupload = request.files.get('fileupload')
		file = fileupload

		fileupload = fileupload.filename

		fullfile = fileupload
		
		APP_ROUTE = os.path.dirname(os.path.abspath(__file__))
		folder = os.path.join(APP_ROUTE, 'static/images/')

		fileupload, file_extension = os.path.splitext(fileupload)

		image_format = file_extension[1:]

		m = hashlib.md5()
		m.update(str(albumid))
		m.update(fullfile)
		picid = m.hexdigest()


		if allowed_file(fullfile):
			cur.execute("INSERT INTO contain (sequencenum, albumid, picid) VALUES (%s, %s, %s)", [sequencenum + 1, albumid, picid])
			cur.execute("INSERT INTO photo (picid, format) VALUES (%s, %s)", [picid, image_format])
			file.save(os.path.join('static/images/', picid + '.' + image_format))


		



	if method == "delete":
		picid = request.form.get('picid')
		albumid = request.form.get('albumid')
		cur.execute("SELECT format FROM photo WHERE picid = %s", [picid])
		pic_format = cur.fetchall()
		pic_format = pic_format[0]['format']


		cur.execute("DELETE FROM contain WHERE picid = %s", [picid])

		cur.execute("DELETE FROM photo WHERE picid = %s", [picid])

		os.remove(os.path.join('static/images/', picid + "." + pic_format))



	cur.execute("SELECT * FROM AlbumAccess WHERE albumid = %s",[albumid])
	usersWithAccess = cur.fetchall()

	cur.execute("SELECT access FROM album WHERE albumid = %s",[albumid])
	tempAccess = cur.fetchall()
	isPrivate = False
	if tempAccess[0]['access'] == 'private':
		isPrivate = True


	options = {
		"users": True,
		"results": results,
		"albumid": albumid,
		"not_edit": False,
		"firstname": firstname,
		"lastname": lastname,
		"owner": owner,
		"owner_rights": owner_rights,
		"pic_format": pic_format,
		"caption_on": caption_on,
		"logged_in": logged_in,
		"pics": pics,
		"title": title,
		"hostValue": host,
		"portValue": port,
		"edit": True,
		"pub_user_albums": pubalbums,
		"usersWithAccess": usersWithAccess,
		"private": isPrivate
	}

	return render_template("album.html", **options)

@album.route('/album', methods=['GET', 'POST'])
def album_route():

	albumid = request.args.get('albumid')
	db = connect_to_database()
	cur = db.cursor()
	

	logged_in = False
	caption_on = False

	current_username = ""

	firstname = ""
	lastname = ""
	if 'username' in session:
		logged_in = True
		current_username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']

	if current_username == "":
		logged_in = False

	grant_access = False
	owner_rights = False
	public = False

	owner = ""
	album_access = 'private'


	host = env['host']
	port = env['port']
	

	cur.execute("SELECT * FROM album WHERE albumid = %s" , [albumid])
	invalidUser = cur.fetchall()
	if not bool(invalidUser):
		abort(404)

	cur.execute("SELECT username, access from album where albumid = %s", [albumid])
	allowed_access = cur.fetchall()
	album_access = allowed_access[0]['access']
	owner = allowed_access[0]['username']

	if album_access == "public":
		grant_access = True
		public = True
	if owner == current_username:
		grant_access = True
		owner_rights = True
	else:
		cur.execute("SELECT username from AlbumAccess where albumid = %s", [albumid])
		allowed_users = cur.fetchall()
		for user in allowed_users:
			user = user['username']
			if current_username == user:
				grant_access = True



	if (logged_in == True) and (grant_access == False):
		abort(403)

	
	if (logged_in == False) and (public == False):
		return redirect("/gu4wdnfe/p3/login")






	cur.execute('SELECT username FROM user')
	results = cur.fetchall()

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()



	cur.execute("SELECT picid, sequencenum FROM contain WHERE albumid = %s" , [albumid])
	pics = cur.fetchall()
	pic_format = []
	all_captions = []
	new_edit = []
	my_caption = ""
	for pic in pics:
		cur.execute("SELECT picid, format, date FROM photo WHERE picid = %s" , [pic['picid']])
		edit = cur.fetchall()

		cur.execute("SELECT caption FROM contain WHERE picid = %s" , [pic['picid']])
		captions = cur.fetchall()
		my_caption = captions[0]['caption']

		edit[0]['caption'] = my_caption
		new_edit = edit[0]

		pic_format.append(new_edit)

	
	if my_caption is not None:
		caption_on = True
	if len(my_caption) == 0:
		caption_on = False
		

	cur.execute("SELECT title FROM album WHERE albumid = %s" , [albumid])
	title = cur.fetchall()
	title = title[0]['title']

	

	options = {
		"users": True,
		"results": results,
		"firstname": firstname,
		"lastname": lastname,
		"owner": owner,
		"owner_rights": owner_rights,
		"albumid": albumid,
		"caption_on": caption_on,
		"not_edit": True,
		"pic_format": pic_format,
		"pics": pics,
		"title": title,
		"logged_in": logged_in,
		"hostValue": host,
		"portValue": port,
		"edit": False,
		"pub_user_albums": pubalbums
	}

	return render_template("album.html", **options)



