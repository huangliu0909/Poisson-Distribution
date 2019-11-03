import numpy as np
import matplotlib.pyplot as plt
import random
import math


def exponential_rand(lamda):
    u = random.uniform(0.0, 1.0)
    return - (1.0/lamda) * math.log(u)


def question_0():
    born = np.zeros(1000)
    death = np.zeros(1000)
    for i in range(1, 1000):
        born[i] = exponential_rand(0.05)
        death[i] = exponential_rand(0.03)
    x = np.arange(0, 1000, 1)
    s = np.zeros(1000)
    t = np.zeros(1000)
    for i in range(1, 1000):
        if born[i] < death[i]:
            s[i] = s[i - 1] + 1
            t[i] = t[i - 1] + born[i]
        else:
            s[i] = s[i - 1] - 1
            t[i] = t[i - 1] + death[i]
    y = np.zeros(1000)
    for i in range(1, 1000):
        if t[i] > 1000:
            for j in range(int(t[i - 1]), 1000):
                y[j] = s[i - 1]
            break
        for j in range(int(t[i - 1]), int(t[i])):
            y[j] = s[i - 1]

    plt.plot(x, y)
    plt.show()


def question_1():

    num = 1000

    w = np.zeros(num)
    t = np.zeros(num)
    for i in range(num):
        t[i] = exponential_rand(0.05)

    # plt.plot(np.arange(0, 1000), t)
    # plt.show()
    for i in range(1, num):
        # print(i)
        w[i] = w[i - 1] + t[i]
    x = np.arange(1, w[num - 1])
    x_t = np.zeros(int(w[num - 1]))
    for i in range(1, num):
        for j in range(int(w[i - 1]), int(w[i])):

            x_t[j] = i - 1
            # print(i - 1)
    count_1 = 0
    count_2 = 0
    total = 0
    for i in range(1, num):
        if w[i] < 10000:
            if w[i] - w[i - 1] < 10:
                count_1 += 1
            if w[i + 1] - w[i - 1] < 10:
                count_2 += 1
            total += 1
        else:
            break
    print("在10s内发生一次的概率：" + str(count_1 / total))
    print("在10s内发生两次的概率：" + str(count_2 / total))

    x_p = np.zeros(1000)
    y_p = np.zeros(1000)
    for i in range(1000):
        x_p[i] = x[i]
        y_p[i] = x_t[i]

    plt.plot(x_p, y_p)
    plt.show()


question_0()
question_1()