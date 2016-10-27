from flask import *
from extensions import *
from config import *

pic = Blueprint('pic', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@pic.route('/pic', methods = ['GET', 'POST'])
def pic_route():


	db = connect_to_database()
	cur = db.cursor()

	specific_login = False

	current_username = ""

	if 'username' in session:
		specific_login = True
		current_username = session['username']

	if current_username == "":
		specific_login = False

	options = {
		"specific_login": specific_login
	}



	return render_template("single_page.html", **options)


