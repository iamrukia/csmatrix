"""
Problem 1.7.3: my_function_composition(f,g)
input: two functions f and g, represented as dictionaries, such that g * f exists
output: dictionary that represents the function g * f
example: given f = {0:'a', 1:'b'} and g = {'a':'apple', 'b': 'banana'}, return {0:'apple', 1:'banana'}
"""


def my_function_composition(f, g):
    return {x: g[f[x]] for x in f.keys()}


# test the code
f = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
g = {'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}
print(my_function_composition(f, g))
