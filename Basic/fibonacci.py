def main(n):
    a=0
    b=1
    if n>=1:
        print(a)
    if n>=2:
        print(b)
    for i in range(n):
        c=a+b;
        a=b
        b=c
        print(c)