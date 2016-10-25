from flask import *
from extensions import *
from config import *

import hashlib

album = Blueprint('album', __name__, template_folder='templates')

@album.route('/gu4wdnfe/p3/album/edit', methods=['GET', 'POST'])
def album_edit_route():

	UPLOAD_FOLDER = '/static/images'
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'bmp', 'gif'])


	albumid = request.args.get('albumid')
	method = request.form.get('op')

	db = connect_to_database()
	cur = db.cursor()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()
	host = env['host']
	port = env['port']


	cur.execute("SELECT sequencenum FROM contain ORDER BY sequencenum DESC")
	sequencenum = cur.fetchall()
	sequencenum = sequencenum[0]['sequencenum']


	if method == "add":
		albumid = request.form.get('albumid')
		filename = request.form.get('filename')
		print "filename"
		print filename
		#image_format = 
		m = hashlib.md5()
		m.update(str(albumid))
		m.update(filename)
		picid = m.hexdigest()


		cur.execute("INSERT INTO contain (sequencenum, albumid, picid) VALUES (%s, %s, %s)", [sequencenum + 1, albumid, picid])
		cur.execute("INSERT INTO photo (picid, format) VALUES (%s, %s)", [picid, image_format])



	if method == "delete":
		picid = request.form.get('picid')
		albumid = request.form.get('albumid')
		cur.execute("DELETE FROM contain WHERE sequencenum = %s and albumid = %s", [sequencenum, albumid])
		cur.execute("DELETE FROM photo WHERE picid = %s", [picid])




	cur.execute("SELECT picid, sequencenum FROM contain WHERE albumid = %s" , [albumid])
	pics = cur.fetchall()


	cur.execute("SELECT title FROM album where albumid = %s" , [albumid])
	title_sql = cur.fetchall()
	title = title_sql[0]['title']




	options = {
		"users": True,
		"results": results,
		"albumid": albumid,
		"not_edit": False,
		#"pic_format": pic_format,
		"pics": pics,
		"title": title,
		"hostValue": host,
		"portValue": port,
		"edit": True
	}

	return render_template("album.html", **options)

@album.route('/gu4wdnfe/p3/album', methods=['GET', 'POST'])
def album_route():

	albumid = request.args.get('albumid')
	print "albumid"
	print albumid

	db = connect_to_database()
	cur = db.cursor()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()
	host = env['host']
	port = env['port']


	cur.execute("SELECT picid, sequencenum FROM contain WHERE albumid = %s" , [albumid])
	pics = cur.fetchall()
	#i = 0
	#for pic in pics:
		#cur.execute("SELECT format FROM photo WHERE picid = %s" , [pic])
		#pic_format = cur.fetchall()
		#pic_format[i] = pic_format[0]['format']
		#i = i + 1


	cur.execute("SELECT title FROM album where albumid = %s" , [albumid])
	title_sql = cur.fetchall()
	title = title_sql[0]['title']


	

	options = {
		"users": True,
		"results": results,
		"albumid": albumid,
		"not_edit": True,
		#"pic_format": pic_format,
		"pics": pics,
		"title": title,
		"hostValue": host,
		"portValue": port,
		"edit": False
	}

	return render_template("album.html", **options)


