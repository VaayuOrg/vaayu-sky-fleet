# User endpoints

from flask import Blueprint
from api.controller import Route_Controller

class UserRoutes:
    def __init__(self, app):
        user_bp = Blueprint('user', __name__, url_prefix='/user')
        self.controller = Route_Controller()

        # Route: Register new user
        user_bp.add_url_rule('/register', view_func=self.controller.register_user, methods=['POST'])

        # Route: Get user by ID
        user_bp.add_url_rule('/<string:user_id>', view_func=self.controller.get_user, methods=['GET'])

        # Route: Update user
        user_bp.add_url_rule('/<string:user_id>', view_func=self.controller.update_user, methods=['PUT'])

        # Route: List all users
        user_bp.add_url_rule('/', view_func=self.controller.list_users, methods=['GET'])

        # Route: Delete user
        user_bp.add_url_rule('/<string:user_id>', view_func=self.controller.delete_user, methods=['DELETE'])

        # Route: Trigger user DB and collection initialization manually (optional)
        user_bp.add_url_rule('/<string:user_id>/init', view_func=self.controller.init_user_workspace, methods=['POST'])

        # Register blueprint
        app.register_blueprint(user_bp)
