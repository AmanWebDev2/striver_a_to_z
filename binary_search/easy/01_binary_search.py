def search(nums: list[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def bs(nums:list[int],left,right,target):
    if left > right:
        return

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        left = mid + 1
    else:
        right = mid - 1

    return bs(nums,left,right,target)

nums = [3,4,6,7,9,12,16,17]
print(bs(nums,0,len(nums)-1,4))