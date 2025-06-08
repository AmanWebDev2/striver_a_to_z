# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle(self,head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        if fast:
            return slow.next
        return slow
    
    def rev(self,head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # single node
        if head is None or head.next is None:
            return True

        middleNode = self.middle(head)
        revHead = self.rev(middleNode)

        # compare
        curr = head
        while curr.val == revHead.val:
            if curr.next is None and revHead.next is None:
                return True
            curr = curr.next
            revHead = revHead.next
        return False
        