# T.C = O(nlogn)
def brute(nums:list[int]):
    nums.sort()
    return nums[-1]

# T.C = O(n)
def optimal(nums:list[int]):
    largest = nums[1]
    for num in nums:
        largest = max(largest,num)
    return largest
