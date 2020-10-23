# Given an Array, find 4 numbers from it, such that their product is
# Maximum

def solution(A):
    D={}
    for i in range(len(A)):
        D[i]=A[i]
    N=[]
    for i in A:
        if i<0:
            N.append(i)
    P=[]
    for i in A:
        if i>0:
            P.append(i)
    N.sort()
    P.sort()
    N01=n[0]*n[1]
    N23=n[2]*n[3]
    P01=p[-1]*p[-2]
    P23= p[-3] * p[-4]
    mx={'N01':N01,'N23':N23,'P01':P01,'P23':P23}
    mx.sort()
    print(mx)