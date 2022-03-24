import random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a, q, d, k = 3141592, 10, 8, 200
    p = [3, 11, 13, 19, 21, 27, 29, 37, 53, 59, 61, 67, 77, 83, 91]
    t = random.randint(-100, 100)
    k = 200 * t + random.randint(-1, 2) * p[random.randint(0, len(p))]
    rand_arr = []
    for _ in range(100):
        temp = k * a / (q ** d)
        a = (temp - int(temp)) * 10 ** (len(str(temp - int(temp))) - 2)
        rand_arr.append(a / 10 ** len((str(a))))
    print('\n'.join(map(str, rand_arr)))
    math_wait = sum(rand_arr) / len(rand_arr)
    print(f'Матожидание: {math_wait}')
    dispersion = sum([(x - math_wait) ** 2 for x in rand_arr])
    print(f'Дисперсия: {dispersion / (1 / (len(rand_arr) - 1))}')
    inter_length = (max(rand_arr) - min(rand_arr)) / 10
    print(f'Длина интервала: {inter_length}')
    intervals = [min(rand_arr)]
    for i in range(10):
        intervals.append(intervals[i] + inter_length)
    frequency_dict = dict()
    for i in range(1, len(intervals)):
        counter = 0
        for var in rand_arr:
            if intervals[i - 1] <= var <= intervals[i]:
                counter += 1
        frequency_dict[f'{intervals[i - 1]} - {intervals[i]}'] = counter
    print()
    relative_frequency = [x / 100 for x in frequency_dict.values()]
    print(frequency_dict)
    print(relative_frequency)
    print(sum(relative_frequency))
    plt.hist(frequency_dict.values(), density=True, bins=10)
    plt.show()
