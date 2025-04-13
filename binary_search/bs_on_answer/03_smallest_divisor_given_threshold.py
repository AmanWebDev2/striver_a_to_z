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