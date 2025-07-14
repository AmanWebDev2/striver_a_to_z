# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
