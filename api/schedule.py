from flask import jsonify
from flask_classful import FlaskView
from clients.schedule_client import ScheduleClient
from serializers.schedule_serializer import ScheduleSerializer

class ScheduleView(FlaskView):
    def index(self):
        schedule_client = ScheduleClient()
        schedule_client.get_schedule()
        return jsonify(ScheduleSerializer(schedule_client.schedule).serialize())
        