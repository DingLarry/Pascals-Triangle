"""
The Problem is Pasaclas Triangle, and the logic here is pretty straight forward, the number of next line is the sum of two adjacent 
number in previous line.
"""
#Code here
def triangles(num) :
    n,L = 1,[]
    while n <= num :
        n,L = n+1 , [1 if (i == 0 or i == len(L)) else L[i-1] + L[i] for i in range(len(L)+1)]
        yield L
    return
