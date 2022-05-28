import time

from algorithms.base_algorithm import BaseAlgorithm


class Karatsuba(BaseAlgorithm):
    def __init__(self, **kwargs):
        super(Karatsuba, self).__init__(**kwargs)
        self.complexity_svg: str = '/static/img/complexity/karatsuba_complexity.svg'

        self.start_time: float = time.perf_counter()
        self.multiplication_result: str = self.__calculate_multiplication(
            x_number=self.x_number,
            y_number=self.y_number
        )
        self.finish_time: float = time.perf_counter()

    def __str__(self):
        return 'Karatsuba'

    @staticmethod
    def zero_pad(number_string, zeros, left=True):
        """Return the string with zeros added to the left or right."""
        for i in range(zeros):
            if left:
                number_string = '0' + number_string
            else:
                number_string = number_string + '0'
        return number_string

    def __calculate_multiplication(self, x_number: int, y_number: int):
        """Multiply two integers using Karatsuba's algorithm."""
        # convert to strings for easy access to digits
        x = str(x_number)
        y = str(y_number)
        # base case for recursion
        if len(x) == 1 and len(y) == 1:
            return int(x) * int(y)
        if len(x) < len(y):
            x = self.zero_pad(x, len(y) - len(x))
        elif len(y) < len(x):
            y = self.zero_pad(y, len(x) - len(y))
        n = len(x)
        j = n // 2
        # for odd digit integers
        if (n % 2) != 0:
            j += 1
        b_zero_padding = n - j
        a_zero_padding = b_zero_padding * 2
        a = int(x[:j])
        b = int(x[j:])
        c = int(y[:j])
        d = int(y[j:])
        # recursively calculate
        ac = self.__calculate_multiplication(x_number=a, y_number=c)
        bd = self.__calculate_multiplication(x_number=b, y_number=d)
        k = self.__calculate_multiplication(x_number=a + b, y_number=c + d)
        A = int(self.zero_pad(str(ac), a_zero_padding, False))
        B = int(self.zero_pad(str(k - ac - bd), b_zero_padding, False))
        return A + B + bd

