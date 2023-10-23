from flask import Blueprint
from controllers.user import createUser, readUser, readOneUser, upgradeUser, removeUser

user = Blueprint('user', __name__)

@user.route('/user', methods=['POST'])
def addUser():
    return createUser()


@user.route('/user/', methods=['GET'])
def getUsers():
    return readUser()

@user.route('/user/<id>', methods=['GET'])
def getUser(id):
    return readOneUser(id)


@user.route('/user/<id>', methods=['PUT'])
def updateUser(id):
    return upgradeUser(id)

@user.route('/user/<id>', methods=['DELETE'])
def deleteUser(id):
    return removeUser(id)