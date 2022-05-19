import math
import time


def k_mul(x, y):
    if (x < 10) or (y < 10):
        return x * y
    else:
        x_str = str(x)
        y_str = str(y)
        x_num = len(x_str)
        y_num = len(y_str)
        max_len = max(x_num, y_num)
        split_positon = int(max_len / 2)
        x_high, x_low = int(x_str[:-split_positon]), int(x_str[-split_positon:])
        y_high, y_low = int(y_str[:-split_positon]), int(y_str[-split_positon:])

        part1 = k_mul(x_high, y_high)
        part2 = k_mul(x_low, y_low)
        part3 = k_mul((x_high + x_low), (y_high + y_low))

    return (part1 * 10 ** (2 * split_positon)) + ((part3 - part1 - part2) * 10 ** (split_positon)) + part2


def get_finished_time(x: int, y: int, ordinary=False):
    start_time = time.process_time_ns()

    if ordinary:
        print(x * y)
    else:
        print(k_mul(x, y))

    finish_time = time.process_time_ns()

    print(f"Finished in {finish_time - start_time} seconds..")


if __name__ == '__main__':
    start_time = time.perf_counter()

    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    print("Karatsuba..")
    get_finished_time(x, y)

    print("Ordinary..")
    get_finished_time(x, y, True)


