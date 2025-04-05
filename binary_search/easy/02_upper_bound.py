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

def upper_bound_easy(arr,target):
	n = len(arr)
	left = 0
	right = n-1
	ans = -1
	while left <= right:
		mid = left + (right - left) // 2
		if arr[mid] == target:
			ans = mid
			left = mid + 1
		elif target > arr[mid]:
			left = mid + 1
		else:
			right = mid - 
	# if ans == -1 we can return the len of an array
	return ans
arr = [2, 2, 2, 3, 4, 2]
target = 22
print(upper_bound_easy(arr,target))