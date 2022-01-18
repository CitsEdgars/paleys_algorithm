from numpy import *

with open('ieeja.txt', 'r') as infile:
    for line in infile:
        p = int(line)

n = p + 1
x = []
for i in range(n-1):
    x.append((i**2)%(n-1))

x = sorted(list(dict.fromkeys(x)))
matrix = array([[0]*n]*n)

for i in range(n): matrix[0][i] = 1
for j in range(n): matrix[j][0] = -1
for i in range(n): matrix[i][i] = 1

sub_matrix = array([[0]*(n-1)]*(n-1))
sub_matrix[0][0] = 1

for i in range(1,n-1):
    if (i in x):
        sub_matrix[0][i] = -1
    else:
        sub_matrix[0][i] = 1

shiftable = list(sub_matrix[0])

for i in range(1,n-1):
    shiftable = [shiftable.pop(n-2)] + shiftable
    sub_matrix[i] = shiftable

for i in range(1,n):
    for j in range(1,n):
        matrix[i][j] = sub_matrix[i-1][j-1]

with open('izeja.txt', 'w') as outfile:
    for row in matrix:
        for col in list(row):
            outfile.write("{} ".format(col))
        outfile.write("\n")