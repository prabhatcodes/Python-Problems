# Write a program to swap two numbers without using third variable

def swap(x, y):
    print("Before swapping, x=", x, "and y=", y)
    x = x + y
    y = x - y
    x = x - y
    print("After swapping, x=", x, "and y=", y)
