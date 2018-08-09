from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

jwt = JWTManager()

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    if identity.username == 'admin':
        return {'roles': 'xadminx'}
    else:
        return {'roles': 'user'}

@jwt.user_identity_loader
def add_identity_to_access_token(identity):
    print identity.username