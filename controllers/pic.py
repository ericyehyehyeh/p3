from flask import *
from extensions import *
from config import *

pic = Blueprint('pic', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@pic.route('/pic', methods = ['GET', 'POST'])
def pic_route():

	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']
	
	logged_in = False

	current_username = ""

	if 'username' in session:
		logged_in = True
		current_username = session['username']
		cur.execute("SELECT * FROM user WHERE username = %s",[current_username])
		query = cur.fetchall()
		firstname = query[0]['firstname']
		lastname = query[0]['lastname']

	if current_username == "":
		logged_in = False


	options = {
		"logged_in": logged_in, 
		"firstname": firstname, 
		"lastname": lastname
	}


	return render_template("single_page.html", **options)


