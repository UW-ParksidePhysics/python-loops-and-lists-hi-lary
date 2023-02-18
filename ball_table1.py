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
while t_values <= b:
    y = (v * t_values) - 0.5 * g * t_values ** 2
    print(t_values, y)

#for i in array:
    #t = a + i * h
    #t_values.append(t)

#for t in t_values:
    #y = (v * t) - 0.5 * g * t ** 2
   # print(f'{t}, {y}')




