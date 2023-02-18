# exercise 2.7
import numpy as np

v = 1                                   # initial velocity m/s
g = 9.81                                # acceleration due to gravity m/s/s
a = 0                                   # lower limit
b = (2 * v) / g                         # upper limit
n = eval(input('num of intervals:'))    # number of desired intervals
h = (b - a) / n                         # interval length
array = np.arange(0, n + 1, 1)          # start value , stop - 1, intervals
t_values = []

for i in array:
    t = a + i * h
    t_values.append(t)

#while t <= b:
    #y = (v * t) - 0.5 * g * t ** 2

print(t_values)


