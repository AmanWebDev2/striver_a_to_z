def optimal(nums):
    count = 0
    max_count = 0
    for num in nums:
        if num == 0:
            max_count = max(max_count,count)
            count = 0
        else:
            count += 1
    return max(max_count,count)
