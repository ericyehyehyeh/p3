from flask import *
from extensions import *
from config import *


logout = Blueprint('logout', __name__, template_folder='templates')

@logout.route('/gu4wdnfe/p3/logout', methods = ['GET','POST'])
def logout_route():
	session.clear()
	return redirect("/gu4wdnfe/p3/")