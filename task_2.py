import random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x_vars = [2, 3, 5, 8, 11, 15, 20]
    p_vars = [0.1, 0.15, 0.25, 0.05, 0.05, 0.3, 0.1]
    intervals = [0, p_vars[0]] + [sum(p_vars[:i]) + p_vars[i] for i in range(1, len(p_vars))]
    random_arr = [random.random() for _ in range(100)]
    discret_random_arr = []
    frequency_dict = dict().fromkeys(x_vars, 0)
    for var in random_arr:
        for i in range(1, len(intervals)):
            if intervals[i - 1] <= var < intervals[i]:
                discret_random_arr.append(x_vars[i - 1])
                frequency_dict[x_vars[i - 1]] += 1
    math_wait = sum([x_vars[i] * p_vars[i] for i in range(len(x_vars))])
    print(f'Матожидание: {math_wait}')
    dispersion = sum([x_vars[i] ** 2 * p_vars[i] for i in range(len(p_vars))])
    print(f'Дисперсия: {dispersion}')
    plt.hist(discret_random_arr, bins=len(x_vars))
    plt.show()