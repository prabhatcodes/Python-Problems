def fact(n):
    prod=1
    if n==0:
        return(1)
    for i in range(1,n+1):
        prod=prod*i
    return(prod)