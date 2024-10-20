from flask import Blueprint
from controllers.post import create_post, findAllPosts

post_bp = Blueprint('post', __name__) #Blueprint

post_bp.route('/post', methods=['POST'])(create_post)

post_bp.route('/post', methods=['GET'])(findAllPosts)