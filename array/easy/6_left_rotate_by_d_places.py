# T.C = O(n)
# S.C = O(d)
def brute(nums:list[int],d:int):
    n = len(nums)
    d = d % n

    temp = []

    for i in range(d):
        temp.append(nums[i])

    # shifting
    for i in range(d,n):
        nums[i-d] = nums[i]

    # put back
    j = n-d
    for num in temp:
        arr[j] = num
        j += 1

# T.C = O(n)
# S.C = O(1)
def better(nums:list[int],d:int):
    d = d % n
    rev(nums,0,d-1)
    rev(nums,d,len(nums)-1)
    rev(nums,0,len(nums)-1)

def rev(nums,i,j):
    while i < j:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
        j -= 1
