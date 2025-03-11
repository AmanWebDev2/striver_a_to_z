# T.C = O(n)
def left_rotate(nums:list[int]):
    temp = nums[0]
    for i in range(1,len(nums)):
        nums[i-1] = nums[i]

    nums[-1] = temp
