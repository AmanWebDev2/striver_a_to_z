def lower_bound(arr,target):
	n = len(arr)
	left = 0
	right = n-1
	while left <= right:
		mid = left + (right-left) // 2
		if arr[mid] >= target:
			right = mid-1
		else:
			left = mid+1
	return left
nums = [1,1,3,3,7,8,9,9,9,11]
n = len(nums)

import bisect
print(bisect.bisect_left(nums,12))
print(lower_bound(nums,12))


def lower_bound_easy(arr,target):
	n = len(arr)
	left = 0
	right = n-1
	ans = -1
	while left <= right:
		mid = left + (right-left)//2
		if arr[mid] == target:
			ans = mid
			right = mid - 1
		elif target > arr[mid]:
			left = mid + 1
		else:
			right = mid -1
	return ans
arr = [2, 3, 3, 3, 4, 2]
target = 3
print(lower_bound_easy(arr,target))