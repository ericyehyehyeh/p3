from flask import *
from extensions import *
from config import *
import os#possibly delete

logout_api = Blueprint('logout_api', __name__, template_folder='templates')


@logout_api.route('/gu4wdnfe/p3/api/v1/logout', methods=['POST'])
def logout_route():
	if 'username' in session:
		session.clear()
		return jsonify(), 204
	else:
		json_error = {
			"errors":[
						{
							"message": "You do not have the necessary credentials for the resource"
    					}
    				]
    			}
		return jsonify(json_error), 401