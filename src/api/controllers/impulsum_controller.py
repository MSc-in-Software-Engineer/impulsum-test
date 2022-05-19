from flask import jsonify


class ImpulsumController:
    def __init__(self):
        pass

    def post(self, body):
        return jsonify({
            "status": True,
            "message": body
        }), 200
