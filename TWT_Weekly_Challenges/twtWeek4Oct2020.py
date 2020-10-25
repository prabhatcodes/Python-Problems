# Count Black Cells
# Imagine a white grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:
#
# A cell is painted black if it has at least one point in common with the diagonal;
# Otherwise, a cell is painted white.
# Count the number of cells painted black.
# Example:
# >>> solution(3, 4)
# 6
# Because there are 6 cells that have at least one common point with the diagonal and therefore are painted black (see image below).
# https://cdn.discordapp.com/attachments/534693705442131988/767433843396444210/example1.png
# Submission and grading
# - code must be written in python
# - code must be in a function named solution
# - function must take in two integer arguments (n and m)
# - function must return an integer
# - no imports/libraries allowed

def solution(m,n):
    if m==n:
        s=m+2*(m-1)
    else:
        if m%2!=0 and n%2!=0:

        s=max(m,n)+spe

# XXXXXXXXXXXXXXXXXXX the problem was very easy afterall

def sol(m,n):
    return max(m, n) + 2 * (min(m, n) - 1)

# Wrong when tested... very wrong infact

def solution(m,n):
    return m+n+hcf(max(m,n),min(m,n))-2
def hcf(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

# Solution with nested lambda

solution=lambda a,b:a+b+(g:=lambda a,b:g(b,a%b)if b else a)(a,b)-2


# Shortest

def solution(n,m):
 a=n+m
 while m:n,m=m,n%m
 return a+n-2
