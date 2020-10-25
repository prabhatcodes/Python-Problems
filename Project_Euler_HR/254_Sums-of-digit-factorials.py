# https://www.hackerrank.com/contests/projecteuler/challenges/euler254/problem

# Define  as the sum of the factorials of the digits of . For example, .
#
# Define  as the sum of the digits of . So .
#
# Define  to be the smallest positive integer  such that . Though  is ,  is also , and it can be verified that  is .
#
# Define  as the sum of the digits of . So .
#
# Further, it can be verified that  is  and  is .
#
# What is ? As the number can be large, print it modulo .
#
# Input Format
#
# The first line of each test file contains a single integer , which is the number of queries per test file.  lines follow, each containing two integers separated by a single space:  and  of the corresponding query.
#
# Constraints
#
# Output Format
#
# Print exactly  lines, each containing a single integer, which is the answer to the corresponding query.
#
# Sample Input 0
#
# 2
# 3 1000000
# 20 1000000
# Sample Output 0
#
# 8
# 156

def f(n):
    s = 0
    for i in str(n):
        s += fac(int(i))
    return s


def fac(n):
    product: int = 1
    if n == 0:
        return product
    else:
        for i in range(1, n + 1):
            product *= i
    return product

def sf(n):
    sum_of_fn=0
    for i in str(f(n)):
        sum_of_fn+=i
    return sum_of_fn

