# Program to check happy number
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 82 is a happy number number

def check_happy(n):
    sum = 0
    num = n
    while sum != num:
        for i in str(n):
            sum += int(i)**2
        if sum == 1:
            print(n,"is a happy number")
        else:
            num = sum
            sum = 0

----


def isHappyNumber(num):
    rem = sum = 0;

    # Calculates the sum of squares of digits
    while (num > 0):
        rem = num % 10;
        sum = sum + (rem * rem);
        num = num // 10;
    return sum;


num = 82;
result = num;

while (result != 1 and result != 4):
    result = isHappyNumber(result);

# Happy number always ends with 1
if (result == 1):
    print(str(num) + " is a happy number");
# Unhappy number ends in a cycle of repeating numbers which contain 4
elif (result == 4):
    print(str(num) + " is not a happy number");
