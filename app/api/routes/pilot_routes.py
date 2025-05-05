# Pilot endpoints

from flask import Blueprint
from api.controller import Route_Controller

class PilotRoutes:
    def __init__(self, app):
        pilot_bp = Blueprint('pilot', __name__, url_prefix='/pilot')
        self.controller = Route_Controller()

        pilot_bp.add_url_rule('/register', view_func=self.controller.register_pilot, methods=['POST'])
        pilot_bp.add_url_rule('/<int:pilot_id>', view_func=self.controller.get_pilot, methods=['GET'])
        pilot_bp.add_url_rule('/<int:pilot_id>', view_func=self.controller.update_pilot(), methods=['PUT'])
        pilot_bp.add_url_rule('/', view_func=self.controller.list_pilots(), methods=['GET'])

        app.register_blueprint(pilot_bp)
