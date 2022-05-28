import json

from flask import jsonify

from algorithms.karatsuba import Karatsuba
from algorithms.schoolbook import Schoolbook


class ImpulsumController:
    def __init__(self):
        pass

    @staticmethod
    def wrapper_algorithm_multiplication_call(body, class_name):
        multiplication_results: list = []

        input_index = 1
        for input_number in body:
            input_x_y = input_number.get(f'input_{input_index}')

            result = {
                'inputs': f'{input_index}. Inputs',
                'results': class_name(
                    x_number=input_x_y.get('x'),
                    y_number=input_x_y.get('y'),
                ).get_multiplication_result(),
            }

            input_index += 1
            multiplication_results.append(result)

        return multiplication_results

    def post(self, body, bulk):
        try:
            if bulk == 0:
                algorithm_id: str = body.get('algorithm_id')
                x_num: int = body.get('x_num')
                y_num: int = body.get('y_num')

                if algorithm_id == 'karatsuba':
                    karatsuba = Karatsuba(x_number=x_num, y_number=y_num)
                    return jsonify({"status": True, "result": karatsuba.get_multiplication_result()})
                elif algorithm_id == 'schoolBook':
                    schoolbook = Schoolbook(x_number=x_num, y_number=y_num)
                    return jsonify({"status": True, "result": schoolbook.get_multiplication_result()})

            if bulk == 1:
                results = {
                    'algorithms': [
                        {'name': 'Karatsuba',
                         'result': self.wrapper_algorithm_multiplication_call(body=body, class_name=Karatsuba)},
                        {'name': 'Schoolbook',
                         'result': self.wrapper_algorithm_multiplication_call(body=body, class_name=Schoolbook)}
                    ]
                }

                return jsonify({
                    "status": True,
                    "results": results
                }), 200

            return jsonify({
                "status": True,
                "message": body
            }), 401

        except Exception as e:
            print(e)
            return jsonify({
                "status": False,
                "error_message": str(e)
            }), 500
