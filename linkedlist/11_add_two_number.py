class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        dummy = ListNode(-1)
        curr = dummy
        carry = 0

        while t1 or t2:
            sum = carry
            if t1:
                sum += t1.val
            if t2:
                sum += t2.val

            newNode = ListNode(sum%10)
            carry = sum // 10

            curr.next = newNode
            curr = curr.next

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next

        if carry:
            newNode = ListNode(carry)
            curr.next = newNode

        return dummy.next
