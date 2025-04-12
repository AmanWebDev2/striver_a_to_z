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