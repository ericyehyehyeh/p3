from flask import *
from extensions import *
from config import *

pic = Blueprint('pic', __name__, template_folder='templates', url_prefix='/gu4wdnfe/p3')

@pic.route('/pic', methods = ['GET', 'POST'])
def pic_route():



	return render_template("single_page.html", **options)


