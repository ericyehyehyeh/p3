from flask import *
from extensions import *
from config import *

pic = Blueprint('pic', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p2')

@pic.route('/pic', methods = ['GET', 'POST'])
def pic_route():

	logged_in = False

	if 'username' in session:
		logged_in = True
		current_username = session['username']


	picid = request.args.get('picid')

	db = connect_to_database()
	cur = db.cursor()
	cur.execute("SELECT picid FROM photo WHERE picid = %s" , [picid])
	invalidUser = cur.fetchall()
	if not bool(invalidUser):
		abort(404)
		
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



	cur.execute("SELECT sequencenum FROM contain where picid = %s", [picid])
	sequencenum = cur.fetchall()
	sequencenum = sequencenum[0]['sequencenum']


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
	

	options = {
		"last": last,
		"first": first,
		"users": True,
		"results": results,
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

