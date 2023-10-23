from flask import Flask
from dotenv import load_dotenv
import os

from config.database import mongo
from routes.users import user

config = load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo.init_app(app)

app.register_blueprint(user, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(port = 5000, debug = True, host = '0.0.0.0')