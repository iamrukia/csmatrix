"""
Problem 1.7.8: myUnion(L)
input: list of sets
output: the union of all sets in L
"""


def myUnion(L):
    result_set = set()
    for item_set in L:
        result_set = result_set | item_set
    return result_set


# test the code
L = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}, {11, 12, 13}]
print(myUnion(L))
