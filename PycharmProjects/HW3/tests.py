import numpy as np
import math

first = np.array([[0.9950928, 0.99027794],[1.0246571, 1.00796825]])
second = np.array([[0.5,0.001]])


def find_func3_nominator(b_t, b_t_j ,learning_rate, x_t, x_t_j):
    print(math.exp((learning_rate * x_t_j)))
    print(b_t_j * float(math.exp((learning_rate * x_t_j))))
    y = (np.dot(b_t, x_t))
    return b_t_j * math.exp((learning_rate * x_t_j))/y

b_t = [[0.5, 0.5]]
b_t_j = b_t[0][0]
b_t = b_t[0]

learning_rate = 0.5
x = [[0.9950928 , 0.99027794], [1.0246571 , 1.00796825]]
x_t = x[0]
x_t_j =  x_t[0]
print(x_t, 'x_t')
print(type(b_t_j))
find_func3_nominator(b_t, b_t_j ,learning_rate, x_t, x_t_j)
"""i = 0
mul =first[i, :]  * second
print(first)
print(second)
print(mul)
print(b_t)
"""
