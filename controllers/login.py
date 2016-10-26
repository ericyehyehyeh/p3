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
	
	return render_template("login.html")

