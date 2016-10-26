from flask import *
from extensions import *
from config import *
import hashlib
import uuid
import os#possibly delete

album_api = Blueprint('album_api', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')



@album_api.route('/api/v1/album/<albumid>', methods=['GET'])
def album_route(albumid):

	albumid = albumid;
	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']

	current_username = ""
	firstname = ""
	lastname = ""

	if 'username' in session:
		current_username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']


	grant_access = False
	owner_rights = False
	public = False

	owner = ""
	album_access = 'private'


	cur.execute("SELECT * FROM album WHERE albumid = %s" , [albumid])
	invalidUser = cur.fetchall()
	if not bool(invalidUser):
		json_error = {
				"errors":[
						{
							"message": "The requested resource could not be found"
    					}
    				]
    			}
    	return jsonify(error = json_error), 404


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
		json_error = {
				"errors":[
						{
							"message": "You do not have the necessary permissions for the resource"
    					}
    				]
    			}
    	return jsonify(error = json_error), 403
    	
	if (logged_in == False) and (public == False):
		json_error = {
				"errors":[
						{
							"message": "You do not have the necessary credentials for the resource"
    					}
    				]
    			}
    	return jsonify(error = json_error), 401


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

		cur.execute("SELECT caption, sequencenum FROM contain WHERE picid = %s" , [pic['picid']])
		capt_seq = cur.fetchall()
		my_caption = capt_seq[0]['caption']
		my_sequencenum = capt_seq[0]['sequencenum']

		edit[0]['caption'] = my_caption
		edit[0]['sequencenum'] = my_sequencenum
		new_edit = edit[0]

		pic_format.append(new_edit)

		
	if my_caption is not None:
		caption_on = True
	if len(my_caption) == 0:
		caption_on = False
			

	cur.execute("SELECT title, created, lastupdated FROM album WHERE albumid = %s" , [albumid])
	json_data = cur.fetchall()
	title = json_data[0]['title']
	created = json_data[0]['created']
	lastupdated = json_data[0]['lastupdated']



	my_data = {
		"access": album_access,
		"albumid": albumid,
		"created": created,
		"lastupdated": lastupdated,
		"pics": new_edit,
		"title": title,
		"username": current_username
		}

	return jsonify(my_data)





