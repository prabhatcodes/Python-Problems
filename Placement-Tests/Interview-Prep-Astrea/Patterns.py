# *
# **
# ***
# ****
# *****
# ****** for N

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print ("*", end='')
        print()

# 1
# 12
# 123
# 1234
# 12345 for N

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print()

# 1
# 22
# 333
# 4444
# 55555

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print()

# 55555
# 4444
# 333
# 22
# 1

def pattern(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(i, end="")
        print()

# 11111
# 2222
# 333
# 22
# 1

def pattern(n):
    k=1
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(k, end="")
        k+=1
        print()

# 55555
# 5555
# 555
# 55
# 5

def pattern(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1)
            print(n, end="")
        print()

# 1
# 21
# 321
# 4321
# 54321

def pattern(n):
    k=n
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(k, end="")
        print()

# 54321
# 4321
# 321
# 21
# 1

def pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()