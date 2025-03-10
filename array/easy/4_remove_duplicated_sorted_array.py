# T.C = O(n)
def remove_dupli(nums:list[int]):
    if n == 1:
        return n

    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
