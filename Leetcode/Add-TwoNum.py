# You are given two non-empty linked lists
# representing two non-negative integers.
# The digits are stored in reverse order,
# and each of their nodes contains a single digit.
# Add the two numbers and return the
# sum as a linked list.

# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

# Initial Solution

def addTwoNumbers(l1, l2):
    num1 = 0
    num2 = 0
    for i in range(-1, -len(l1)-1, -1):
        num1 = (num1 * 10) + l1[i]
    for i in range(-1, -len(l2)-1, -1):
        num2 = (num2 * 10) + l2[i]
    summ = str(num1 + num2)
    sol = []
    for i in range(-1, -len(summ)-1, -1):
        sol.append(int(summ[i]))
    return sol

# After learning new concept

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next