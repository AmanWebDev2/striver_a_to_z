import math

"""
    Time Complexity: O(1)
    Space Complexity: O(1)
"""
def approach_1(n):
    return math.floor(math.sqrt(n))

"""
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
"""
def approach_2(n):
    ans = n
    for i in range(1,n):
        if i * i <= n:
            ans = i
        else:
            break
    return ans

"""
    Time Complexity: O(log n)
    Space Complexity: O(1)
"""
def approach_3(n):
    left = 1
    right = n // 2
    ans = n

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans