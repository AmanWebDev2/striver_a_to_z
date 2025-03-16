# T.C = O(n^2)
def brute(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return [-1,-1]

# T.C = O(nlogn) + O(n)
def better(nums,target):
    nums.sort()
    i = 0
    j = 0

    while i<j:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            return [i,j]
    return [-1,-1]

# T.C = O(n)
# S.C = O(n)
def optimal(nums,target):
    mpp = dict()
    for i,num in enumerate(nums):
        rem = target - num
        if rem in mpp:
            return [i,mpp.get(rem)]
        mpp[num] = i

    return [-1,-1]
