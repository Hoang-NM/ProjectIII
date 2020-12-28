import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


data = pd.read_csv("dataset.csv")
N, d = data.shape
x = data[:, 0:d - 1].reshape(-1, d - 1)
y = data[:, 2].reshape(-1, 1)

x_cho_vay = x[y[:, 0] == 1]
x_tu_choi = x[y[:, 0] == 0]

plt.scatter(x_cho_vay[:, 0], x_cho_vay[:, 1], c='red', edgecolor='none', s=30, label='cho vay')
plt.scatter(x_tu_choi[:, 0], x_tu_choi[:, 1], c='blue', edgecolor='none', s=30, label='từ chối')
plt.legend(loc=1)
plt.xlabel(u'mức lương (triệu)')
plt.ylabel(u'knh nghiệm (năm)')

x = np.hstack((np.one(N, 1), x))

w = np.array([0., 0.1, 0.1]).reshape(-1, 1)

numOfIteration = 1000
cost = np.zeros((numOfIteration, 1))
learning_rate = 0.01

for i in range(1, numOfIteration):
    y_predict = sigmoid(np.dot(x, w))
    cost[i] = -np.sum(np.multiply(y, np.log(y_predict)) + np.multiply(1 - y, np.log(1 - y_predict)))
    # Gradient Descent
    w = w - learning_rate * np.dot(x.T, y_predict - y)
    print(cost[i])

t = 0.5
plt.plot((4, 10), (-(w[0] + 4 * w[1] + np.log(1 / t - 1)) / w[2], -(w[0] + 10 * w[1] + np.log(1 / t - 1)) / w[2]), 'g',
         label='t=0.5')
t = 0.8
plt.plot((4, 10), (-(w[0] + 4 * w[1] + np.log(1 / t - 1)) / w[2], -(w[0] + 10 * w[1] + np.log(1 / t - 1)) / w[2]), 'g',
         label='t=0.8')
plt.legend(loc='upper right')
plt.show()
