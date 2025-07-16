from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1: Reverse the Linked List and then calculate the decimal value
class Solution:
    def rev(self, head):
        if head is None or head.next is None:
            return head
        last = self.rev(head.next)
        head.next.next = head
        head.next = None
        return last

    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        last = self.rev(head)
        temp = last
        power = 0
        num = 0
        while temp:
            num += pow(2, power) * temp.val
            temp = temp.next
            power += 1
        return num


# Approach 2: Bit Manipulation
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        temp = head
        while temp:
            num = num << 1 | temp.val
            temp = temp.next
        return num


# Approach 3:
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = ""
        temp = head
        while temp:
            num += str(temp.val)
            temp = temp.next

        return int(num, 2)
