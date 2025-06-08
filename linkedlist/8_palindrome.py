# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    curr = None
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        

        i = 0
        j = len(arr)-1
        while i<j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True