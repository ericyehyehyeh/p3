from flask import *
from extensions import *
from config import *
import hashlib
import uuid



login = Blueprint('login', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

#@login.route('/login' , methods = ['GET','POST']")
@login.route('/login')
def login_route():
	if 'username' in session:
		return redirect("/gu4wdnfe/p3/user/edit")
	
	db = connect_to_database()
	cur = db.cursor()

	post_requested = False

	cur.execute("SELECT * FROM album WHERE access = 'public'")
	pubalbums = cur.fetchall()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()
	
	options = {
		"pub_user_albums": pubalbums,
		"results": results,
	}

	return render_template("login.html", **options)

