from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.decorators.auth_jwt_decorator import *
from app.entities.user import *
from app.services.userService import *
import bcrypt

auth = Blueprint('AuthController', __name__, url_prefix='/auth')

user_service = userService()

@auth.route("/register", methods=["POST"])
def register():
	input_data = request.get_json()
	user_email = input_data['email']
	user_password = input_data['password']
	user_role = input_data['role']

	input_user = user(user_email,user_password,user_role)
	return user_service.user_register(input_user)


@auth.route('/login', methods=['POST'])
def login():
	
	input_data = request.get_json()
	user_email = input_data['email']
	user_password = input_data['password']

	return user_service.login_check(user_email,user_password)


@auth.route("/protected", methods=["GET"])
@jwt_required() #jwt check
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    claims = get_jwt()
    return jsonify(logged_in_as=current_user), 200



@auth.route("/admin", methods=["GET"])
@jwt_required()    # jwt check
@admin_required()  # role : admin check
def admin_test():
    current_user = get_jwt_identity()    
    return jsonify(logged_in_as=current_user), 200



@auth.route("/user", methods=["GET"])
@jwt_required()    # jwt check
@user_required()   # role : user check
def user_test():
    current_user = get_jwt_identity()  
    return jsonify(logged_in_as=current_user), 200