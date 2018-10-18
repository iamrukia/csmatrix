"""
Problem 0.8.2 cubes(L)
input: list L of number
output: list of numbers in which the ith element is the cube of the ith element of L
Example: given [1,2,3] return [1,8,27]
"""


def cubes(L):
    return [x ** 3 for x in L]


# test the code
test_list = list(range(10))
print(cubes(test_list))
