# T.C = O(n)
def check(nums:list[int]):
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            return True
    return False
