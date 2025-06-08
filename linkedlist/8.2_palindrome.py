# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def compare(self,prev,head):
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # single node or empty
        if head is None or head.next is None:
            return True

        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            nxt = slow.next
            slow.next = prev
            prev = slow

            fast = fast.next.next
            slow = nxt
        
        # compare 
        # odd no of nodes
        if fast:
            return self.compare(prev,slow.next)
        
        return self.compare(prev,slow)