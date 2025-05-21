from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from os import environ
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure CORS
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('SECRET_KEY', 'your-secret-key-here')

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import User

# Replace before_first_request with a better initialization approach
with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return {'message': 'Hello, PlanVenture!'}

if __name__ == '__main__':
    app.run(debug=True)