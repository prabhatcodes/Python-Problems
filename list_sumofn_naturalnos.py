# Natural Sum and Queries
# You are given  queries. In each query you are given an integer , you have to tell whether there exists some positive integer , such that  can be represented as sum of first  natural numbers.
#
# Mathematically,
#
# Input Format
#
# First line of the input contains a single integer  (Number of queries).
#
# Each of the next  lines, contains a single integer .
#
# Constraints
#
#
#
# Output Format
#
# For each query, print on a seperate line "Yes" if there exists some  else print "No". (without quotes)
#
# Sample Input 0
#
# 3
# 1
# 2
# 3
# Sample Output 0
#
# Yes
# No
# Yes

Q = input()
X = []
for i in range(int(Q)):
    x = input()
    X.append(int(x))


def summ(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


for j in X:
    con = 0
    flag = 0
    while con <= j:
        for i in range(1, j + 1):
            if summ(i) == j:
                print("Yes")
                flag = 1
                break
            else:
                con = summ(i)
    if flag == 0:
        print("No")