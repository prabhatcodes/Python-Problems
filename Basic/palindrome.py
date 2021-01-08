def pal(m):
    org=[]
    for i in m:
        org.append(i)
    rev=[]
    for i in range(-1,-len(org)-1,-1):
        rev.append(org[i])
    if rev==org:
        print("Palindrome!")
    else:
        print("Not a Palindrome!")