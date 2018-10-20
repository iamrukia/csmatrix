"""
Problem 0.8.4: inv_dict(d)
input: dictionary d representing an invertible function f
output: dictionary representing the inverse of f, the returned dictionary's keys are the values of d and its values are the keys of d
example: given an English-French dictionary
{'thank you': 'merci', 'goodbye': 'au revoir'}
return a French-English dictionary
{'merci':'thank you', 'au revoir':'goodbye'}
"""


def inv_dict(d):
    return {d[k]: k for k in d.keys()}


# test the code
d = {'thank you': 'merci', 'goodbye': 'au revoir'}

print(inv_dict(d))
