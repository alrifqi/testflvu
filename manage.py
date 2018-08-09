__author__ = 'alrifqi'
from app import manager
from app.modules.models import User, db
from werkzeug.security import generate_password_hash

@manager.command
def seed():
    # user = User(name='test', username='test', password=generate_password_hash('test'), email='test@test.com', handphone='12345678', gender='m')
    admin= User(name='admin', username='admin', password=generate_password_hash('admin'), email='admin@admin.com',
                handphone='88888888', gender='m')
    # db.session.add(user)
    db.session.add(admin)
    db.session.commit()

if __name__ == '__main__':
    manager.run()