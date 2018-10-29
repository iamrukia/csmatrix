"""
Problem 1.7.4: mySum(L)
input: list of numbers
Output: sum of numbers in the list
"""


def mySum(L):
    my_sum = 0
    for i in L:
        my_sum = my_sum + i
    return my_sum


# test the code
L = [x for x in range(50)]
print(L)
print(mySum(L))
