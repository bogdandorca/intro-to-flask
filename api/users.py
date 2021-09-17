from flask import jsonify
from app import app, db
from models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def getAllUsers():
    users = User.query.all()
    return jsonify([e.serialize() for e in users])

def createUser(user_details):
    try:
        user_model = User(
            username = user_details['username'],
            email = user_details['email'],
            password = bcrypt.generate_password_hash(user_details['password'].encode('utf8')).decode('utf8'),
            active = False
        )

        db.session.add(user_model)
        db.session.commit()

        return {
            'message': 'User has been created'
        }
    except Exception as e:
        return {
            'message': 'There has been a problem with the request'
        }, 500

def getUserById(id_):
    try:
        user = User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
        return str(e), 500

def logIn(username, password):
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            return 'Invalid credentials'

        if not bcrypt.check_password_hash(user.getPassword(), password):
            return 'Invalid credentials'

        return user.serialize()
    except Exception as e:
        return str(e), 500