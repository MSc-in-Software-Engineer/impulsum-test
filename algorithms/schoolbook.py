import time

from algorithms.base_algorithm import BaseAlgorithm


class Schoolbook(BaseAlgorithm):
    def __init__(self, **kwargs):
        super(Schoolbook, self).__init__(**kwargs)

        self.complexity_svg: str = '/static/img/complexity/schoolbook_complexity.svg'

        self.start_time: float = time.perf_counter()
        self.multiplication_result: int = self.__calculate_multiplication(
            x_number=self.x_number,
            y_number=self.y_number
        )
        self.finish_time: float = time.perf_counter()

    def __str__(self):
        return 'Schoolbook'

    def __calculate_multiplication(self, x_number: int, y_number: int):
        return int(int(x_number) * int(y_number))
