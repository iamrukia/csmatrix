"""
Problem 0.8.5: First write a procedure row(p, n) with the following spec:
input: integer p, integer n

output: n-element list such that element i is p + i

example: given p = 10 and n = 4, return [10, 11, 12, 13]
Next write a comprehension whose value is a 15-element list of 20-element lists such that the jth element of the ith
list is i + j. You can use row(p, n) in your comprehension.

Finally, write the same comprehension but without using row(p, n) Hint: replace the call to row(p,n) with the
comprehension that forms the body of row(p, n)
"""


def row(p, n):
    return [i + p for i in list(range(n))]


def next_row():
    return [row(i, 20) for i in range(15)]


def final_row():
    return [[i + p for i in list(range(20))] for p in range(15)]


# test the code
result_list = final_row()

print(result_list[3][4])
print(result_list[2][5])
print([result_list[a][b] for a in range(15) for b in range(20)])
