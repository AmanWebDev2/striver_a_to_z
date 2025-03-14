# T.C = O(n^2)
def brute(nums):
    for num in nums:
        count = 0
        for n in nums:
            if n == num:
                count += 1
        if count == 1:
            return num
    return -1

# T.C = O(n)
# S.C = O(max(nums))
def better(nums):
    n = len(nums)
    max_num = max(nums)+1
    hash = [0] * max_num
    for num in nums:
        hash[num] += 1
    for num in hash:
        if num == 1:
            return num
    return -1

# T.C = O(n)
# S.C = O(n)
def better2(nums):
    mpp = dict()
    for num in nums:
        mpp[num] = 1 + mpp.get(num,0)
    for k,v in mpp.items():
        if v == 1:
            return k
    return -1


# T.C = O(n)
# S.C = O(1)
def optimal(nums):
    a = 0
    for num in nums:
        a ^= num
    return a
