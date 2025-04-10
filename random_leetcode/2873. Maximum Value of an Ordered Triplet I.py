'''
Brute force:
- O(n^3) time complexity
- O(1) space complexity
'''
def brute(nums):
    max_val = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                max_val = max(max_val, (nums[i] - nums[j]) * nums[k])
    return max_val

'''
Better:
- O(n) time complexity
- O(n) space complexity
'''
def better(nums):
    n = len(nums)
    left_max = [0] * n
    right_max = [0] * n

    for i in range(1,n):
        left_max[i] = max(nums[i-1],left_max[i-1])
    
    for i in range(n-2,-1,-1):
        right_max[i] = max(nums[i+1],right_max[i+1])
    
    max_triplet = 0
    for i in range(1,n):
        max_triplet = max(max_triplet,(left_max[i]-nums[i])*right_max[i])
    
    return max_triplet