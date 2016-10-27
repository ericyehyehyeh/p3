from flask import *
from extensions import *
from config import *
import hashlib
import uuid



login = Blueprint('login', __name__, template_folder='templates')

#@login.route('/login' , methods = ['GET','POST']")
@login.route('/gu4wdnfe/p3/login', methods = ['GET'])
def login_route():
	if 'username' in session:
		return redirect("/gu4wdnfe/p3/user/edit")
	return render_template("login.html")

