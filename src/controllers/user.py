from flask import request, jsonify, Response
from bson import json_util, ObjectId

from flask_jwt_extended import jwt_required, get_jwt_identity

from config.database import mongo

def createUser(): #Add user
    try:
        fullname = request.json['fullname']
        username = request.json['username']
        password = request.json['password']

        isRegister = mongo.db.user.find_one({'username': username})

        if isRegister:
            return jsonify({'msg': f'User {isRegister["username"]} added previously'}), 400

        user = mongo.db.user.insert_one({
            'fullname': fullname, 'username': username, "password": password
        })

        return jsonify({'msg': f'User {str(user.inserted_id)} added successfully'}), 200
    except Exception as e:
        return jsonify({ 'msg': f'Error {str(e)}' }), 500


def findAllUser(): #Get users
    try:
        data = mongo.db.user.find()
        return json_util.dumps(data), 200
    except Exception as e:
        return jsonify({ 'msg': f'Error {str(e)}' }), 500


def findOneUser(id): #Get user
    try:
        user = mongo.db.user.find_one({'_id': ObjectId(id)})
        if user:
            return json_util.dumps(user), 200
        else:
            return jsonify({'msg': 'Resource not found'}), 400
    except Exception as e:
        return jsonify({ 'msg': f'Error {str(e)}' }), 500


@jwt_required()
def editUser(id): #Update user
    try:
        user = mongo.db.user.find_one({'_id': ObjectId(id)})
        if user:
            data = request.get_json()
            mongo.db.user.update_one({'_id': ObjectId(id)}, {'$set': data})
            return jsonify({'msg': f'User {id} update successfully'}), 200
        else:
            return jsonify({'msg': 'Resource not found'}), 400
    except Exception as e:
        return jsonify({ 'msg': f'Error {str(e)}' }), 500


@jwt_required()
def removeUser(id): #Remove user
    try:
        user = mongo.db.user.find_one({'_id': ObjectId(id)})
        if user:
            mongo.db.user.delete_one({'_id': ObjectId(id)})
            return jsonify({'msg': f'User {id} deleted successfully'}), 200
        else:
            return jsonify({'msg': 'Resource not found'}), 400
    except Exception as e:
        return jsonify({ 'msg': f'Error {str(e)}' }), 500