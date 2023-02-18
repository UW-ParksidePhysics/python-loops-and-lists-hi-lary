# exercise 2.6
import numpy as np

a = eval(input('a value:'))           # lower limit
b = eval(input('b value:'))           # upper limit
n = eval(input('num of intervals:'))  # number of desired intervals
h = (b - a) / n                       # interval length
array = np.arange(0, n + 1, 1)        # start value , stop - 1, intervals
empty_list = []

for i in array:
    x = a + i * h
    empty_list.append(x)
print(empty_list)
