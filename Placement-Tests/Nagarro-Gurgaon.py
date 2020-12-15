# 15-12-2020
# Company came through University Placement cell.
# Was required to fill a Google Form to apply for the test.

# For Automation Testing at Gurgaon Office.

# Job Profile:  Trainee, Technology

# Stipend:  Students will be paid a stipend of Rs 15,000 per month at the time of training.
# The CTC to be offered after the training completion is 3.50 LPA.

# Selection Process:  Aptitude test and technical objective test of 60 minutes followed by a programming test
# of 90 minutes (All rounds will be elimination rounds).
# The shortlisted candidates will be eligible for the virtual interview process.

# Students can use any language in which they are comfortable with.

# Experience

# Test took place on Mettl Platform. Screensharing, Webcam and Microphone was on for the whole time.
# 1 hour for Aptitude Test (25 questions) and DSA (15 questions).
# Aptitude Questions were decent; neither too hard, nor too easy.
# In DSA many questions were on Sorting and their complexities.
# Good thing was that it didn't ask questions on a particular language. They used pseudo-code.

# Programming Part consisted of 3 Questions, 1 very easy, and 2 easy. And had to solve in 1:30 hours.
# One question had a faulty default test case. Wasted a lot of time on it, before actually reading the
# test case and realizing it's Expected Output was wrong.

# Was able to correctly solve all 3 problems in Python3.

# Problem 1. Question: Cut m letters from the end of string then add it at the front of the string, then
# cut n letters from the end of the modified string and add to the beginning.
# Continue this process till you get back the original string and return total turns it took.

# Given are a string and m and n.
#
# input 1: original string

# input 2: m (less than length of string): cut m alphabets from end of string and then
# add to beginning of string.

# input 3: n (less than length of string) : cut n alphabets from end of string obtained
# from above step and then add to beginning of that string.
#
# This process is continued, need to find out the number turns it takes to get back original string.

# Example : Input-> Arya, 1, 2 Gives Output -> 3

# Solving: TBH this problem took me the most time.

def main(input1, input2, input3):
    org = list(input1)
    l = len(org)
    m = input2
    n = input3
    mod = org
    count = 0
    flag = 0
    while flag == 0:
        count += 1
        if count%2 == 1:
            temp = []
            temp = mod[l-m:l]
            mod = mod[0:l-m]
            mod = temp + mod
            if mod == org:
                return count
        else:
            temp = []
            temp = mod[l-n:l]
            mod = mod[0:l-n]
            mod = temp + mod
            if mod == org:
                return count

# Problem 2: Given an array consisting of integers, return the longest strictly increasing substring.
# Note: This problem had a wrong test case.

# Input 1: Number of integers in array. Type: Integer.
# Input 2: Array.

# Example: Input-> 5, {1,2,3,1,5} Output-> 3

def main(input1, input2):
    n = input1
    A = input2
    count = 1
    max_count = 1
    for i in range(0,n-1):
        if A[i+1] > A[i]:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 1
    return max_count

# Problem 3: A guy donates money for n days. Each ith day he donates i^2 coins.
# Return the total number of coins he donates after n days.

# Input1: Number of days. Type: Integer.

# Example: Input-> 4 Output-> 30

# Easiest Question

def main(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i
    return sum