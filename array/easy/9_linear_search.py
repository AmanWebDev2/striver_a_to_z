def brute(nums:list[int],target):
    for i,num in enumerate(nums):
        if num == target:
            return i
    return -1
