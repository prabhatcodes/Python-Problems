# Challenge 23: In 2120!
# you are walking with your friend to stumble upon an old
# computer that looks like something a century old but somehow
# it still has an old script that works.
# you and your friend start inputing random numbers into it
# and it either outputs True or False.
# you and your friend start wondering about the algorithm behind
# this old mystery piece of tech and go in to try to solve it
#
# >>> solution(902200100)
# ... True
# >>> solution(11000)
# ... False
# >>> solution(99080)
# ... True
# >>> solution(1022220)
# ... True
# >>> solution(106611)
# ... True
# >>> solution(234230)
# ... False
# >>> solution(888)
# ... False
# >>> solution(100)
# ... False
# >>> solution(1000000000)
# ... False
# >>> solution(103456789)
# ... True

# Extra testcases in a dictionary
# https://hastebin.com/uyekakular.yaml

def Solution(n):
    ns=str(n)
    f=False
    for i in range(len(ns)):
        if ns[i]==0:
            for j in range(i,len(ns)):
                if ns[j] in [1,2,3,4,5,6,7,8,9]:
                    f=True
                    break
    return(f)

