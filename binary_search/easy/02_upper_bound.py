def upper_bound(arr,target):
	n = len(arr)
	left = 0
	right = n-1
	while left <= right:
		mid = left + (right - left) // 2
		if arr[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return left

arr = [1, 3, 5, 7, 9]
target = 15
print(upper_bound(arr, target))  # Output: 3 (index of 7)
