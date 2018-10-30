"""
Problem 1.7.6: myMin(L)
input: list of numbers
output: minimum number in the list
"""


def myMin(L):
    min_value = L[0]
    for x in L:
        min_value = x if x < min_value else min_value
    return min_value


# test the code
L = [123, 3465, 123, 12, 3432, 54, 4,
     532, 98, 7, 45, 7, 87, 43657, 8956, 3, 64265, 4, 78, 6, 543534, 6, 567, 87, 43, 234, 5, 457786, 4, 3, 457, 3, 234,
     1, 54, 7687, 12, 9, 85342, 5, 87, 4, 2, 56768, ]
print(myMin(L))