from app import app, db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    active = db.Column(db.Boolean)

    def __init__(self, username, email, password, active):
        self.username = username
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'active': self.active
        }

    def getPassword(self):
        return self.password
