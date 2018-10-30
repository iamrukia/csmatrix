"""
Problem 1.7.5: myProduct(L)
input: list of numbers
output: product of numbers in the list
"""


def myProduct(L):
    result = 1
    for x in L:
        result = result * x
    return result


# test the code
L = [1, 2, 3, 4, 5, 6, 7, 8, 10, 13]
print(myProduct(L))
