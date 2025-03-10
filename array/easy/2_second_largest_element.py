# T.C = O(nlogn) + O(n)
def brute(nums:list[int]):
    nums.sort()
    largest = nums[-1]
    for i in range(n-2,-1,-1):
        if nums[i] != largest:
            return nums[i]

def better(nums:list[int]):
    largest = nums[0]
    second_largest = -sys.maxsize-1
    for num in nums:
        largest = max(largest,num)

    for num in nums:
        if num > second_largest and num != largest:
            second_largest = num

    return second_largest

def optimal(nums:list[int]):
    largest = nums[0]
    second_largest = -1

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        else:
            if num > second_largest and num != largest:
                second_largest = num

    return second_largest
