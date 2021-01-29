# Print numbers from 0-100, if number is divisible by 3 then print
# fizz instead and if number is divisible by 5 then print buzz.
# if number is divisible by both 3 & 5 then print fizzbuzz.

def fizzbuzz1():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("buzz")
        else:
            print(i)


def fizzbuzz2():
    for i in range(1, 101):
        d = ""
        if i % 3 == 0:
            d += "fizz"
        if i % 5 == 0:
            d += "buzz"
        if d == "":
            print(i)
        else:
            print(d)

def fizzbuzz3(): # without modulo
    c3 = 0
    c5 = 0
    for i in range(1,101):
        c3+=1
        c5+=1
        d=""
        if c3==3:
            d += "fizz"
            c3=0
        if c5==5:
            d += "buzz"
            c5=0
        if d=="":
            print(i)
        else:
            print(d)