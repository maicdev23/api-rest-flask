import os
from dotenv import load_dotenv

from flask import Flask
from flask_jwt_extended import JWTManager

from config.database import mongo

from routes.user import user_bp
from routes.post import post_bp

config = load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

JWTManager(app)
mongo.init_app(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(post_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(port = 5000, debug = True, host = '0.0.0.0')