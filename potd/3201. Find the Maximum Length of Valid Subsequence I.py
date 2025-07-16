from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)

According to the definition of a valid subsequence, we can observe that all elements at odd indices in the subsequence must have the same parity, and all elements at even indices must also have the same parity. Therefore, there are a total of four possible parity patterns for the subsequence:

All elements are even.
All elements are odd.
Elements at odd indices are odd, and elements at even indices are even.
Elements at odd indices are even, and elements at even indices are odd.
"""


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evenCount = 0
        oddCount = 0
        for num in nums:
            if num % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1

        parity = nums[0] % 2
        alternateCount = 1

        for i in range(1, len(nums)):
            currentParity = nums[i] % 2
            if currentParity != parity:
                alternateCount += 1
                parity = currentParity

        return max(evenCount, oddCount, alternateCount)
