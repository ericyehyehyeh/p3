from flask import *
from extensions import *
from config import *

pic = Blueprint('pic', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@pic.route('/pic', methods = ['GET', 'POST'])
def pic_route():

	logged_in = False

	current_username = ""
	db = connect_to_database()
	cur = db.cursor()
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
	caption_on = False
	public = False
	owner = ""
	album_access = 'private'

	host = env['host']
	port = env['port']
	

	picid = request.args.get('picid')

	cur.execute("SELECT picid FROM photo WHERE picid = %s" , [picid])
	invalidUser = cur.fetchall()
	if not bool(invalidUser):
		abort(404)

	

	cur.execute("SELECT albumid from contain where picid = %s", [picid])
	albumid = cur.fetchall()
	albumid = albumid[0]['albumid']


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
		cur.execute("SELECT username from AlbumAccess where albumid = %s", ['albumid'])
		allowed_users = cur.fetchall()
		for user in allowed_users:
			user = user['username']
			if current_username == user:
				grant_access = True

	if (logged_in == True) & (grant_access == False):
		abort(403)

	if (logged_in == False) & (public == False):
		return redirect("/gu4wdnfe/p3/login")

	

	
		
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()
	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()
	host = env['host']
	port = env['port']
	last = True
	first = True
	pic_format = "jpg"


	try:
		cur.execute("SELECT format FROM photo WHERE picid = %s" , [picid])
		pic_format = cur.fetchall()
		pic_format = pic_format[0]['format']


	except IndexError:
		pic_format = "jpg"



	cur.execute("SELECT albumid FROM contain WHERE picid = %s" , [picid])
	albumid = cur.fetchall()
	albumid = albumid[0]['albumid']



	cur.execute("SELECT username FROM album WHERE albumid = %s" , [albumid])
	username = cur.fetchall()
	username = username[0]['username']



	cur.execute("SELECT title FROM album where albumid = %s", [albumid])
	title = cur.fetchall()
	title = title[0]['title']



	cur.execute("SELECT sequencenum, caption FROM contain where picid = %s", [picid])
	sql_results = cur.fetchall()
	sequencenum = sql_results[0]['sequencenum']
	current_caption = sql_results[0]['caption']


	if current_caption is not None:
		caption_on = True
	


	try:
		cur.execute("SELECT picid FROM contain where albumid = %s and sequencenum = %s", [albumid, sequencenum + 1])
		next_pic = cur.fetchall()
		next_pic = next_pic[0]['picid'] 

	except IndexError:
		next_pic = ""
		last = False;

	try:
		cur.execute("SELECT picid FROM contain where albumid = %s and sequencenum = %s", [albumid, sequencenum - 1])
		prev_pic_arr = cur.fetchall()
		prev_pic = ""
		prev_pic = prev_pic_arr[0]['picid']
	
	except IndexError:
		prev_pic = ""
		first = False;

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()


	new_caption = current_caption
	if request.method == "POST":
		new_caption = request.form.get('new_caption')
		cur.execute("UPDATE contain SET caption = %s WHERE picid = %s", [new_caption, picid])
		cur.execute("UPDATE album SET lastupdated = CURRENT_TIMESTAMP WHERE albumid = %s", [albumid])




	options = {
		"last": last,
		"first": first,
		"users": True,
		"firstname": firstname,
		"lastname": lastname,
		"owner_rights": owner_rights,
		"results": results,
		"caption": new_caption,
		"caption_on": caption_on,
		"albumid": albumid,
		"username": username,
		"prev": prev_pic,
		"next": next_pic,
		"title": title,
		"pic_format": pic_format,
		"picid": picid,
		"logged_in": logged_in,
		"hostValue": host,
		"pub_user_albums": pubalbums,
		"results": results,
		"portValue": port,
		"pub_user_albums": pubalbums
	}

	return render_template("pic.html", **options)

