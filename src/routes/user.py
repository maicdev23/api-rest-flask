from flask import Blueprint
from controllers.user import createUser, findAllUser, findOneUser, editUser, removeUser
from controllers.auth import loginUser

user_bp = Blueprint('user', __name__)

@user_bp.route('/auth', methods=['POST'])
def authUser():
    return loginUser()


@user_bp.route('/user', methods=['POST'])
def addUser():
    return createUser()


@user_bp.route('/user/', methods=['GET'])
def getUsers():
    return findAllUser()
    

@user_bp.route('/user/<id>', methods=['GET'])
def getUser(id):
    return findOneUser(id)


@user_bp.route('/user/<id>', methods=['PUT'])
def updateUser(id):
    return editUser(id)


@user_bp.route('/user/<id>', methods=['DELETE'])
def deleteUser(id):
    return removeUser(id)