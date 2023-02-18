# exercise 2.5
import numpy as np
n = eval(input('enter n value:'))
n_values_array = np.linspace(0, n, n + 1)  # starting value, ending value, how many values
initial_value = 0
for i in n_values_array:
    equation = i * (i + 1) / 2
    initial_value += i  # adds and sets equal to the index value
    print(initial_value, equation)
