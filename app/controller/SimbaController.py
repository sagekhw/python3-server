from flask import Blueprint

simba = Blueprint('SimbaController', __name__, url_prefix='/simba')


@simba.route('/a', methods=['GET'])
def a():    
    return {'hello':'a-simba'}

