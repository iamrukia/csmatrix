"""
Task 1.4.17: From the module math, import the definition e and pi.
Let n be the integer 20. Let w be the complex number e2pii/n.
Write a comprehension yielding the list consisting of w0, w1, w2,..., wn-1.
Plot these complex numbers
"""
import math
from math import pi
from math import e
from chap1.plotting import plot

n = 20
w = e ** (2 * pi * 1j / n)

result_list = [w ** counter for counter in range(0, 20, 1)]
plot(result_list, 4)
