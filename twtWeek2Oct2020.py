'''Easy Numbers Challenge

You're walking accross the street and you find a paper with what seems to be math problems. A particular one grabs your interest as you have no idea right of the bat how it could have been possibly done.

>>> print(solution(1))
0
>>> print(solution(5))
4
>>> print(solution(10))
9
>>> print(solution(12))
13
>>> print(solution(34))
57
>>> print(solution(70))
129
>>> print(solution(100))
189
>>> print(solution(58473029386609125789)) # monster case
1158349476621071404669


Task
Write up an algorithm that will be able to solve these examples (do not hard code it because your solution will be tested against many randomly generated integers like that)

Submission and grading
- code must be written in python
- code must be in a function
- function must take in an integer argument (do not take user inputs)
- function must return an integer (do not print it)
- no imports/libraries allowed
'''

def solution(x):
    l=len(str(x-1))
    n=0
    n=x*l-int(str('1'*l))
    return n
    
