
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from clients.schedule_client import ScheduleClient
from api.schedule import ScheduleView

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
db = SQLAlchemy(app)

ScheduleView.register(app)

if __name__ == '__main__':
    app.run()