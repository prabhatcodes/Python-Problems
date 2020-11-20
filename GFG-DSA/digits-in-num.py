# WAP to find the number of digits in a given number in O(1) time

# We know that 10^k-1<=N<10^K
# Therefore floor(log base 10 (N) + 1) is required solution

import math
def digits_in_num(N):
    return math.floor(math.log10(N)+1)