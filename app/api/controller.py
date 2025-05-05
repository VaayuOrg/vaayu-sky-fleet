from flask import request, jsonify
from services.user_service import UserService

class Route_Controller:
    def __init__(self):
        self.user_service = UserService()

    def register_user(self):

        data = request.get_json()
        user_type = data.get('type')  # 'enterprise', 'personal', or 'authority' 
        user_id = data.get('id')      #  expects user id from client-side
        user_data = data.get('user_data')            

        # register user, trigger DB and collection creation
        res = self.user_service.init_user(user_id, user_type, user_data)
        if res:
           return jsonify({'status': 'success', 'message':'user registered successfully'}), 201
        else:
           return jsonify({'status': 'error', 'message': 'an error occured, process aborted'}), 400

    def get_user(self, user_id):
        ...

    def update_user(self, user_id):
        ...

    def list_users(self):
        ...

    def delete_user(self, user_id):
        ...
