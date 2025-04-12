import math

"""
    Time Complexity: O(m * n)
    Space Complexity: O(1)
"""
def brute(piles,h):
    speed = 1
    while True:
        hour_spent = 0

        for pile in piles:
            hour_spent += math.ceil(pile/speed)
        
        if hour_spent <= h:
            return speed
        else:
            speed += 1       


"""
    Time Complexity: O(n * log(max(piles)))
    Space Complexity: O(1)
"""
 
def binary_search(piles,h):
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low + high) // 2
        th = getTotalHours(piles,mid)
        if th <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

def getTotalHours(piles,k):
    th = 0
    for pile in piles:
        th += math.ceil(pile/k)
    return th


print(brute([3,6,7,11],8))
print(binary_search([3,6,7,11],8))