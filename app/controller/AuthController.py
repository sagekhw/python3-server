from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.decorators.auth_jwt_decorator import *
from app.entities.user import *
from app.services.userService import *

auth = Blueprint('AuthController', __name__, url_prefix='/auth')

user_service = userService()

#################################################
# 로그인 API 영역


@auth.route("/register", methods=["POST"])
def register():
	input_data = request.get_json()
	user_email = input_data['email']
	user_password = input_data['password']
	user_role = input_data['role']

	if(user_role == 'role_user' or user_role == 'role_admin'):
		userObj = user(email=user_email,password=user_password,role=user_role)
		result = user_service.insert_by_register(userObj)
		if result:
			return "success"
		else:
			return "false"
	else:
		return jsonify(
			result = "Invalid Params!"
			)


@auth.route('/login', methods=['POST'])
def login():
	
	input_data = request.get_json()
	user_email = input_data['email']
	user_password = input_data['password']

	temp = user_service.readByEmailandPassword(user_email,user_password)

	
	if(temp == "nothing" or temp == "False"):
		return jsonify(
			result = "Invalid Params!"
			)
	else:
		input_role = temp[0]['role']
		if(not input_role):
			return "false"

		additional_claims = {"role": f"{input_role}"}
		return jsonify(result = "success",
			# 검증된 경우, access 토큰 반환
			access_token = create_access_token(identity = user_email,
											additional_claims=additional_claims,
											expires_delta = False)
		)	
	
#################################################
# 회원 전용 API 영역
@auth.route("/protected", methods=["GET"])
@jwt_required() #jwt check
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    claims = get_jwt()
    print(claims["role"])
    print(current_user)
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