# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mpp = dict()
        curr = head
        while curr:
            if mpp.get(curr):
                return True
            mpp[curr] = True
            curr = curr.next
        return False
