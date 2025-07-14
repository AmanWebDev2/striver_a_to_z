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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev(head)
