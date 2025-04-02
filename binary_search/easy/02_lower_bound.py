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