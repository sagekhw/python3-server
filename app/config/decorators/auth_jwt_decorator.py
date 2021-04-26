#   def login_required(f):
#       @wraps(f)
#       def decorated_function(*args, **kwargs):
#           access_token = request.headers.get("Authorization")
#           if access_token is not None:
#               try:
#                   payload = jwt.decode(access_token, app.config["JWT_SECRET_KEY"], "HS256")
#               except jwt.InvalidTokenError:
#                   payload = None
	
#               if payload is None:
#                   return Response(status=401)
	
#               email = payload["email"]
#               g.email = email
#               g.email = get_user_info(email) if email else None
#           else:
#               return Response(status=401)
	
#           return f(*args, **kwargs)
#       return decorated_function
from functools import wraps
from flask_jwt_extended import ( verify_jwt_in_request, jwt_required,  get_jwt_identity, get_jwt)

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] == 'role_admin':
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper

def user_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] == 'role_user':
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Users only!"), 403

        return decorator

    return wrapper