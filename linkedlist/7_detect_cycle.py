# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        P = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != P:
                    P = P.next
                    slow = slow.next
                return P
        return None

    def brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mpp = dict()
        curr = head
        while curr:
            if mpp.get(curr):
                return curr
            mpp[curr] = True
        return None