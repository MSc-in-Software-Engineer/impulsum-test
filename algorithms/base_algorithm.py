import time


class BaseAlgorithm:
    def __init__(self, **kwargs):
        self.x_number: int = kwargs.get('x_number')
        self.y_number: int = kwargs.get('y_number')
        self.complexity_svg: str = ''

        self.start_time: float = time.monotonic()
        self.multiplication_result: int = 0
        self.finish_time: float = time.monotonic()

    def get_multiplication_result(self):
        result_dict = {
            'multiplication_result': self.multiplication_result,
            'execution_time': f"{str(round(self.finish_time - self.start_time + 0.001, 8))} seconds",
            'complexity_svg': self.complexity_svg,
            'x': self.x_number,
            'y': self.y_number
        }

        return result_dict
