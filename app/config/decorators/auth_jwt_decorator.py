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