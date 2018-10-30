"""
Problem 1.7.7: myConcat(L)
input: list of strings
output: concatenation of all the string in L
"""


def myConcat(L):
    myConcat_string = ''
    for x in L:
        myConcat_string = myConcat_string + x
    return myConcat_string


# test the code
L = ['abc', 'asdf', 'asejkr', 'pibjvcue', 'niuadh7jxjd', 'sabnxujc9ewqj', '8eh']
print(myConcat(L))
