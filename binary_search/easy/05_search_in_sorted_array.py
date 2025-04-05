def find_pivot(arr):
	n = len(arr)
	left = 0
	right = n-1
	while left < right:
		mid = left + (right-left) // 2
		if arr[mid] > arr[right]:
			left = mid + 1
		else:
			right = mid
	return left

def bs(arr,target,left,right):
	n = len(arr)

	while left <= right:
		mid = left + (right-left) // 2
		if arr[mid] == target:
			return mid
		elif target > arr[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return -1

def search(nums,target):
	pivot_idx = find_pivot(nums)
	idx = bs(nums,target,0,pivot_idx-1)
	if idx != -1:
		return idx
	idx = bs(nums,target,pivot_idx,len(nums)-1)
	return idx

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
print(search(nums,target))
	