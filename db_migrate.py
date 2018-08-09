__author__ = 'alrifqi'
from app.modules.models import db
from app.modules.models import Client, Token, User

db.create_all()

user = User(
    name='reza',
    username='reza',
    email='reza.nurrifqi@aersure.com',
    password='test'
)

client = Client(
    name='confidential',
    client_id='confidential',
    client_secret='confidential',
    _redirect_uris='http://localhost:8080/oauth/authorized',
    user=user,
)

token = Token(
    user=user,
    client=client
)

db.session.add(user)
db.session.add(client)
db.session.add(token)
db.session.commit()


#
# access_token = conn.Token()
# access_token['user'] = user
# access_token['client'] = client
# access_token.save()
# return 'success', 200
