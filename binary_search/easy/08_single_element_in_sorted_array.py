# T.C: O(n)
# S.C: O(1)
def brute(nums):
	n = len(nums)
	for i in range(0,n-2,2):
		if nums[i] != nums[i+1]:
			return nums[i]
	return -1

# T.C: O(n)
# S.C: O(1)
def approach2(nums):
	xor = 0
	for num in nums:
		xor ^= num
	return xor

# T.C: O(logn)
# S.C: O(1)
def approach_binary_search(nums):
	n = len(nums)
	l = 0
	r = n-1

	while l < r:
		mid = l + (r-l)//2
		is_even = (r - mid) % 2 == 0

		if nums[mid] == nums[mid+1]:
			if is_even:
				# go right
				l = mid + 1
			else:
				# go left
				r = mid-1

		else:
			if is_even:
				# go left
				r = mid
			else:
				l = mid + 1
	return nums[l]
