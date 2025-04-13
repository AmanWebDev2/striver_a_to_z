import math

"""
    Time Complexity: O(n * d)
    Space Complexity: O(1)
"""
def brute(nums,threshold):
    d = max(nums)
    min_divisor = d
    while d > 0:
        ans = 0

        for num in nums:
            ans += math.ceil(num/d)
        
        if ans <= threshold:
            min_divisor = min(min_divisor,d)
        
        d -= 1

    return min_divisor

print(brute([1,2,5,9],6))
# output: 5


def binary_search(nums,threshold):
    low = 1
    high = max(nums)
    ans = high
    def divisorSum(d):
        result = 0
        for num in nums:
            result += math.ceil(num/d)
        return result

    while low <= high:
        mid = (low + high) // 2

        ds = divisorSum(mid)

        if ds <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(binary_search([1,2,5,9],6))
# output: 5