"""
Problem 0.8.3: tuple_sum(A,B)
input: list A and B of the same length, where each element in each list is a pair(x,y) of numbers
output: list of pairs(x,y) in which the first element of the ith pair is the sum of the first element of the ith pair
 in A and the first element of the ith pair in B
example: given lists [(1,2), (10,20)] and [(3,4), (30, 40)], return [(4,6), (40, 60)]
"""


def tuple_sum(A, B):
    result_list = []
    for i in range(len(A)):
        result_list.append((A[i][0] + B[i][0], A[i][1] + B[i][1]))
    return result_list


# test the code
test_tuple_one = [(1, 2), (3, 4), (5, 6), (7, 8)]
test_tuple_two = [(11, 12), (13, 14), (15, 16), (17, 18)]
print(tuple_sum(test_tuple_one, test_tuple_two))
