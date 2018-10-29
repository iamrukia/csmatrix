"""
Problem 1.7.2: my_lists(L)
input: list L of non-negative integers.
output: a list of lists: for every element x in L create a list containing 1,2,...,x.
example: given [1,2,4] return[[1],[1,2],[1,2[3,4]]. example: given[0] return [[]]
"""


def my_lists(L):
    return [list(range(1, x+1)) if x != 0 else [] for x in L]


# test the code
L = [1, 2, 3, 4, 5, 6, 0, 7, 1, 2]
print(my_lists(L))
