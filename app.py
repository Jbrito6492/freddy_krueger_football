
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from clients.schedule_client import ScheduleClient

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
db = SQLAlchemy(app)