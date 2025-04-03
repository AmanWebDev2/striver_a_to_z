def floor(arr,target):
	n = len(arr)
	left = 0
	right = n-1
	ans = -1
	while left <= right:
		mid = left + (right - left)//2
		if arr[mid] <= target:
			ans = arr[mid] # store potential ans
			left = mid + 1 # move right for largest value <= target (floor)
		else:
			right = mid - 1
	return ans

def ceil(arr,target):
	n = len(arr)
	left = 0
	right = n-1
	ans = -1
	while left <= right:
		mid = left + (right - left) // 2
		if arr[mid] >= target:
			ans = arr[mid]
			right = mid - 1 # move left for smallest value >= target (ceil)
		else:
			left = mid + 1
	return ans

arr = [1, 3, 5, 7, 9]
target = 6
print(floor(arr, target))  # Output: 5
print(ceil(arr, target))  # Output: 7
