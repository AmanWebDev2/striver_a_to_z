def min_cost(nums, cost):
    left, right = min(nums), max(nums)
    ans = float('inf')
    while left <= right:
        mid = left + (right - left) // 2
        
        cost1 = get_cost(nums, cost, mid)
        cost2 = get_cost(nums, cost, mid + 1)

        ans = min(cost1, cost2)

        if cost1 < cost2:
            right = mid -1 
        else:
            left = mid + 1
            
    return 0 if ans == float('inf') else ans

def get_cost(nums, cost, x):
    total_cost = 0
    for i,num in enumerate(nums):
        total_cost += abs(num - x) * cost[i]
    return total_cost


print(min_cost([1, 3, 5, 2], [2, 3, 1, 14]))
# print(min_cost([1, 2, 3], [10, 10, 10]))