from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

from model import * 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('dburl')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Welcome to our API"

if __name__ == '__main__':
    app.run(port=5555, debug=True)

