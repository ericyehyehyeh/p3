from flask import *
from extensions import *
from config import *
import hashlib
import uuid
import os#possibly delete

pic_api = Blueprint('pic_api', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')


@pic_api.route('/api/v1/pic/<picid>', methods=['PUT', 'GET'])
def pic_route(picid):

	logged_in = False

	current_username = ""
	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']
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


	my_picid = picid

	if 'username' in session:
		current_username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']



	if request.method == 'GET':
		cur.execute("SELECT picid FROM photo WHERE picid = %s" , [my_picid])
		invalidUser = cur.fetchall()
		if not bool(invalidUser):
			json_error = {
				"errors":[
						{
							"message": "The requested resource could not be found"
    					}
    				]
    			}
    		return jsonify(json_error), 404



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
			json_error = {
				"errors":[
						{
							"message": "You do not have the necessary permissions for the resource"
    					}
    				]
    			}
    		return jsonify(json_error), 403

		if (logged_in == False) & (public == False):
			json_error = {
				"errors":[
						{
							"message": "You do not have the necessary credentials for the resource"
    					}
    				]
    			}
    		return jsonify(json_error), 401



		cur.execute("SELECT format FROM photo WHERE picid = %s", [my_picid])
		format_info = cur.fetchall()
		format_info = format_info[0]['format']

		cur.execute("SELECT * FROM contain WHERE picid = %s", [my_picid])
		pic_info = cur.fetchall()
		albumid = pic_info[0]['albumid']
		sequencenum = pic_info[0]['sequencenum']
		caption = pic_info[0]['caption']


		try:
			cur.execute("SELECT picid FROM contain where albumid = %s and sequencenum = %s", [albumid, sequencenum + 1])
			next_pic = cur.fetchall()
			next_pic = next_pic[0]['picid'] 

		except IndexError:
			next_pic = 1

		try:
			cur.execute("SELECT picid FROM contain where albumid = %s and sequencenum = %s", [albumid, sequencenum - 1])
			prev_pic = cur.fetchall()
			prev_pic = prev_pic[0]['picid']
	
		except IndexError:
			prev_pic = -1




		json_data = {
	  		"albumid": albumid,
	  		"caption": caption,
	  		"format": format_info,
	  		"next": next_pic,
	  		"picid": my_picid,
	 		"prev": prev_pic
		}

		return jsonify(json_data)


	elif request.method == 'PUT':
		if 'username' in session:
			current_username = session['username']
		else:
			json_error = {
				"errors":[
						{
							"message": "You do not have the necessary credentials for the resource"
    					}
    				]
    			}
    		return jsonify(json_error), 401



		data = request.get_json()
		new_caption = data['caption']
		update_picid = data['picid']
		format_info = data['format']
		albumid = data['albumid']
		next_pic = data['next']
		prev_pic = data['prev']

		error = False


		cur.execute("SELECT picid FROM photo WHERE picid = %s" , [update_picid])
		invalidUser = cur.fetchall()
		if not bool(invalidUser):
			error = True
			json_error = {
				"errors":[
						{
							"message": "The requested resource could not be found"
    					}
    				]
    			}
    		return jsonify(json_error), 404


    	cur.execute("SELECT format FROM photo WHERE picid = %s" , [update_picid])
    	current_format = cur.fetchall()
    	current_format = current_format[0]['format']

    	cur.execute("SELECT sequencenum, albumid FROM contain WHERE picid = %s" , [update_picid])
    	current_data = cur.fetchall()
    	current_sequencenum = current_data[0]['sequencenum']
    	current_albumid = current_data[0]['albumid']


    	cur.execute("SELECT picid FROM contain where albumid = %s and sequencenum = %s", [current_albumid, current_sequencenum + 1])
    	next_pic = cur.fetchall()
    	next_pic = next_pic[0]['picid'] 

    	if not bool(next_pic):
    		next_pic = 1

		cur.execute("SELECT picid FROM contain where albumid = %s and sequencenum = %s", [current_albumid, current_sequencenum - 1])
		prev_pic = cur.fetchall()
		prev_pic = prev_pic[0]['picid']

		if not bool(prev_pic):
			prev_pic = -1




    	current_prev = prev_pic
    	current_next = next_pic



    	if current_albumid != albumid:
    		error = True
    	if current_prev != prev_pic:
    		error = True
    	if current_next != next_pic:
    		error = True
    	if current_format != format_info:
    		error = True

    	if error == True:
    		json_error = {
				"errors":[
						{
							"message": "You can only update caption"
    					}
    				]
    			}
    		return jsonify(json_error), 403


    	if error == False:
			cur.execute("UPDATE contain SET caption = %s WHERE picid = %s", [new_caption, update_picid])
			cur.execute("UPDATE album SET lastupdated = CURRENT_TIMESTAMP WHERE albumid = %s", [albumid])


			json_data = {
	  			"albumid": albumid,
	  			"caption": new_caption,
	  			"format": format_info,
	  			"next": next_pic,
	  			"picid": update_picid,
	 			"prev": prev_pic
			}

			return jsonify(json_data)



	#IF EMPTY REQUEST OPTION
	elif request.method == "":
		json_error = {
				"errors":[
						{
							"message": "You did not provide the necessary fields"
    					}
    				]
    			}
    		return jsonify(json_error), 422













