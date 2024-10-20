from flask import request, jsonify
from flask_jwt_extended import create_access_token

from config.database import mongo

def loginUser():
    username = request.json.get('username')
    password = request.json.get('password')

    user = mongo.db.user.find_one({"username": username})
    
    if user and user['password'] == password:
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify(access_token=access_token), 200
    
    return jsonify(message="Bad username or password"), 401