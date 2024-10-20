from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from config.database import mongo

@jwt_required()
def create_post():
    user_id = get_jwt_identity()
    title = request.json.get('title')
    content = request.json.get('content')
    
    mongo.db.posts.insert_one({"user_id": user_id, "title": title, "content": content})
    return jsonify(message="Post created"), 201

@jwt_required()
def findAllPosts():
    posts = mongo.db.posts.find()
    return jsonify(posts=[post for post in posts]), 200