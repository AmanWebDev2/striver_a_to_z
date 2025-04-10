'''
With the rule that "nums[-1] = nums[n] = -∞", we're treating the array conceptually as:
[-∞, 1, 3, 2, 5, 6, 4, -∞]

'''
def approach1(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    # why are we returning len(nums)-1?
    # because if the array is strictly increasing, the last element is a peak
    return len(nums)-1

def approach2(nums):
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid + 1
    return l