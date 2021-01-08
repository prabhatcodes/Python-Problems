def fib(k):
    if k==1:
        return 0
    elif k==2:
        return 1
    elif k>2:
        return fib(k - 1) + fib(k - 2)

def gen_fib(n):
    for i in range(1,n+1):
        print(fib(i))