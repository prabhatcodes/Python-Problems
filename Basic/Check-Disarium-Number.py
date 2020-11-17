# WAP to check if the entered number is Disarium or not
# eg: n = 175
# then 1^1 + 7^2 + 5^2 = 175 (original number)

def checkDisarium(n):
    sum=0
    num=1
    for i in str(n):
        sum = sum + (int(i))**(num)
        num += 1
    if int(sum) == n:
        return "The entered number is a Disarium Number"
    else:
        return "The entered number is not a Disarium Number"