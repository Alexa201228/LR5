import random
import matplotlib.pyplot as plt


def func(x):
    if x == 0 or x == 2 or x == 4:
        return 0
    if 0 < x < 2:
        return 1 / 4 * x
    return 1 / 4 * x - 0.5


if __name__ == '__main__':
    M = 0.5
    a, b = 0, 4
    random_arr = []
    while len(random_arr) < 100:
        x = a + random.random() * (b - a)
        nu = random.random() * M
        if func(x) <= nu:
            random_arr.append(x)
    math_wait = sum(random_arr) / len(random_arr)
    print(f'Матожидание: {math_wait}')
    dispersion = sum([(x - math_wait) ** 2 for x in random_arr])
    print(f'Дисперсия: {dispersion / (1 / (len(random_arr) - 1))}')
    inter_length = (max(random_arr) - min(random_arr)) / 10
    intervals = [min(random_arr)]
    for i in range(10):
        intervals.append(intervals[i] + inter_length)
    frequency_dict = dict()
    for i in range(1, len(intervals)):
        counter = 0
        for var in random_arr:
            if intervals[i - 1] <= var <= intervals[i]:
                counter += 1
        frequency_dict[f'{round(intervals[i], 2)}'] = counter
    print()
    plt.bar(frequency_dict.keys(), frequency_dict.values())
    plt.show()
