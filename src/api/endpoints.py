import json

from flask import current_app as app, request, jsonify

from .controllers.home_controller import HomeController
from utils.base_definitions import API_PREFIX
from .controllers.impulsum_controller import ImpulsumController


@app.route(f'{API_PREFIX}/', methods=['GET'])
def home_api():
    home_controller = HomeController()

    if request.method == 'GET':
        return home_controller.get()

    return jsonify({'status': False, 'message': 'Method Not Allowed! ... [GET] only REQUEST ACCEPTABLE!'}), 405


@app.route(f'{API_PREFIX}/impulsum/<int:bulk>/', methods=['POST'])
def impulsum(bulk: int):
    impulsum_controller = ImpulsumController()

    if request.method == 'POST':
        body = request.get_json()
        return impulsum_controller.post(body=body, bulk=bulk)

    return jsonify({'status': False, 'message': 'Method Not Allowed! ... [POST] only REQUEST ACCEPTABLE!'}), 405
