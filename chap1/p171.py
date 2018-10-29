"""
Problem 1.7.1: my_filter(L, num)
input: list of numbers and a positive integer.
output: list of numbers not containing a multiple of num.
example: given list = [1,2,4,5,7] and num = 2, return [1,5,7].
"""


def my_filter(L, num):
    return [x for x in L if x % num != 0]


# test the code
L = [1, 3, 4, 5, 6, 7, 2, 34, 54, 123, 123, 245, 245, 657, 123, 534, 234, 546, 1234, 7654, 1, 1230]
num = 5

print(my_filter(L, num))
