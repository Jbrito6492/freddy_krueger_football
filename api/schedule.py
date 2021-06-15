from flask import jsonify
from flask_classful import FlaskView, route
from clients.schedule_client import ScheduleClient
from serializers.schedule_serializer import ScheduleSerializer

class ScheduleView(FlaskView):
    @route('/<id>/')
    def get(self, id):
        schedule_client = ScheduleClient(id)
        schedule_client.get_schedule()
        return jsonify(ScheduleSerializer(schedule_client.schedule).serialize())
        