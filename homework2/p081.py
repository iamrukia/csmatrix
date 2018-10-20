"""
Problem 0.8.1 increments(L)
input: list L of numbers
output: list of numbers in which the ith element is one plus the ith element of L
Example: increments([1,5,7]) should return ([2,6,8])
"""


def increments(L):
    return [x + 1 for x in L]


# test the code
test_list = [1, 2, 3, 4, 5, 6]
print(increments(test_list))
