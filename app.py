from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/intro-flask'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from api.users import createUser, getUserById, getAllUsers, logIn

@app.route('/api/user', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return getAllUsers()
    elif request.method == 'POST':
        return createUser(request.json)

@app.route('/api/user/<id_>', methods=['GET'])
def userId(id_):
    return getUserById(id_)

@app.route('/api/login', methods=['POST'])
def logInRoute():
    credentials = request.json
    return logIn(credentials['username'], credentials['password'])

if __name__ == "main":
    app.run(debug=True)
