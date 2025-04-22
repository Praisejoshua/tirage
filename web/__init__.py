from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configurations
app.config["SECRET_KEY"] = "49d36def5362858955171b33"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Triage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {'check_same_thread': False}
}

# Initialize DB
db = SQLAlchemy(app)

