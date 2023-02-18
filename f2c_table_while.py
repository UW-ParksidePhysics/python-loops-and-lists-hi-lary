"""
fahrenheit to Celsius = (f-32)*(5/9)
"""

# exercise 2.1
print('------------------')     # table heading
F = 0                           # start value for F
dF = 10                         # increment of F in loop
while F <= 100:                 # loop heading with condition. We want to end at 100F
    C = (5/9)*(F - 32)          # 1st statement inside loop. Conversion to Celsius
    print(f' {F:0}, {C:0.2f}')  # 2nd statement inside loop. Print the value of F w corresponding value of C.
    F = F + dF                  # 3rd statement inside loop. Edits the printed list to go in increments of 10.

print('------------------')     # end of table line (after loop)
