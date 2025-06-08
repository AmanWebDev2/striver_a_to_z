# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def size(self,head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        length = self.size(head)
        middle = length // 2

        pos = 0
        curr = head
        prev = None

        while curr:
            if pos == middle:
                prev.next = curr.next
                return head
            pos += 1
            prev = curr
            curr = curr.next