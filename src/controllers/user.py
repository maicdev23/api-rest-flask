from flask import request, jsonify, Response
from bson import json_util, ObjectId

from config.database import mongo

def createUser(): #Add user
    try:

        fullname = request.json['fullname']

        existe = mongo.db.user.find_one({'fullname': fullname})

        if existe:
            return jsonify({'msg': f'User {existe["fullname"]} added previously'}), 400

        if fullname:
            user = mongo.db.user.insert_one({ 'fullname': fullname })

            return jsonify({'msg': f'User {str(user.inserted_id)} added successfully'}), 200
    except Exception as e:
        return jsonify(({ 'msg': f'Error {str(e)}' })), 500


def readUser(): #Get users
    try:
        data = mongo.db.user.find()
        return json_util.dumps(data), 200
    except Exception as e:
        return jsonify(({ 'msg': f'Error {str(e)}' })), 500


def readOneUser(id): #Get user
    try:
        user = mongo.db.user.find_one({'_id': ObjectId(id)})
        return json_util.dumps(user), 200
    except Exception as e:
        return jsonify(({ 'msg': f'Error {str(e)}' })), 500


def upgradeUser(id): #Update user
    try:
        data = request.get_json()
        mongo.db.user.update_one({'_id': ObjectId(id)}, {'$set': data})
        return jsonify({'msg': f'User {id} update successfully'}), 200
    except Exception as e:
        return jsonify(({ 'msg': f'Error {str(e)}' })), 500


def removeUser(id): #Remove user
    try:
        mongo.db.user.delete_one({'_id': ObjectId(id)})
        return jsonify({'msg': f'User {id} deleted successfully'}), 200
    except Exception as e:
        return jsonify(({ 'msg': f'Error {str(e)}' })), 500