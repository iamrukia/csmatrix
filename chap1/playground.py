from chap1.image import color2gray, file2image
from chap1.plotting import plot

I = color2gray(file2image('img01.png'))
L = [2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j]
plot(L)

r = len(I)
c = len(I[0])
M = [x + y * 1j for x in range(c) for y in range(r) if I[r - y - 1][x] < 120]
plot(M, max(r, c))
plot([z + (1+2j) for z in L])


plot([z + (50-10j) for z in M], max(r,c))