def brute(weights,days):
    min_weight = max(weights)
    max_weight = sum(weights)
    for capacity in range(min_weight,max_weight+1):
        if can_ship(weights,capacity,days):
            return capacity
    return -1

def can_ship(weights,capacity,days):
    current_weight = 0
    current_day = 1
    for weight in weights:
        if current_weight + weight > capacity:
            current_day += 1
            current_weight = weight
        else:
            current_weight += weight
    return current_day <= days


def optimal(weights,days):
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = low + (high-low) // 2
        if can_ship(weights,mid,days):
            high = mid - 1
        else:
            low = mid + 1
    return low

print(brute([1,2,3,4,5,6,7,8,9,10],5))
print(optimal([1,2,3,4,5,6,7,8,9,10],5))