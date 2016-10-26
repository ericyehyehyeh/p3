from flask import *
from extensions import *
from config import *
import hashlib
import uuid
import re
import os




user = Blueprint('user', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')


@user.route('/user', methods = ['GET','POST'])
def user_route():

	if 'username' in session:
		logged_in = True
		return redirect("/gu4wdnfe/p3/user/edit")


	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']


	options = {
		"new_user": True,
		"edit_user": False,
	}

	print "we're here correct?"

	return render_template("user.html", **options)

@user.route('/user/edit', methods = ['GET','POST'])
def edit_user():

	db = connect_to_database()
	cur = db.cursor()
	host = env['host']
	port = env['port']

	logged_in = False

	if 'username' in session:
		logged_in = True
	else:
		return redirect("/gu4wdnfe/p3/login")


	options = {
		"new_user": False,
		"edit_user": True,
		"logged_in": logged_in
	}



	return render_template("user.html", **options)


