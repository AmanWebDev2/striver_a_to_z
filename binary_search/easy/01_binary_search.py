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