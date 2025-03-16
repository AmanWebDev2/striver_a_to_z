# T.C = O(nlogn)
def brute(nums):
	nums.sort()

# T.C = O(2n)
def better(nums):
	count0 = 0
	count1 = 0
	count2 = 0
	n = len(nums)
	for num in nums:
		if num == 0:
			count0 += 1
		elif num == 1:
			count1 += 1
		else:
			count2 += 1
	for i in range(count0):
		nums[i] = 0

	for j in range(count0,count0+count1):
		nums[j] = 1

	for k in range(count0+count1,n):
		nums[k] = 2

# T.C = O(n)
def optimal(nums):
	n = len(nums)
	low = 0
	mid = 0
	high = n-1

	while mid <= high:
		if nums[mid] == 0:
			nums[low],nums[mid] = nums[mid],nums[low]
			low += 1
			mid += 1
		elif nums[mid] == 1:
			mid += 1
		else:
			nums[mid],nums[high] = nums[high],nums[mid]
			high -= 1
