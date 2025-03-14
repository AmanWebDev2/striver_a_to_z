# T.C = O(n^2)
def brute(nums):
    n = len(nums)
    for i in range(1,n+1):
        if i not in nums:
            return i

def better(nums):
    n = len(nums)
    hash = [0]*(n+1)
    for num in nums:
        hash[num] += 1
    for i,num in enumerate(hash):
        if i==0:
            continue
        if num == 0:
            return 0


# T.C = O(n)
# S.C = O(1)
def optimal1(nums):
    n = len(nums)+1
    expected_sum = (n)*(n+1) // 2 
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# T.C = O(n)
# S.C = O(1)
def optimal2(nums):
    xor1 = 0
    xor2 = 0
    for i,num in enumerate(nums):
        xor1 ^= i+1
        xor2 ^= num
    return xor1 ^ xor2
