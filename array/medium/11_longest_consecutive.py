# T.C = O(n^2)
def brute(nums:list[int]):
	if not nums:
		return 0
	n = len(nums)

	max_count = 1
	for i in range(n):
		count = 1
		ele = nums[i]
		while ele + count in nums:
			count += 1
			max_count = max(max_count,count)
	return max_count

# T.C = O(nlogn) + O(n)
def better(nums:list[int]):
	nums.sort()

	n = len(nums)
	if not nums:
		return 0

	max_count = 1
	count = 1
	for i in range(1,n):
		prev = nums[i-1]
		curr = nums[i]
        
		if prev == curr:
			continue

		if curr - 1 == prev:
			count += 1
			max_count = max(max_count,count)
		else:
			count = 1
	return max_count

# T.C = O(n)
# S.C = O(n)
def optimal(nums):
	n = len(nums)
	if not nums:
	    return 0
	store = set()
	for num in nums:
	    store.add(num)

	max_count = 1

	for elem in store:
	    if elem - 1  not in store:
	        curr = elem
	        count = 1
	        while curr + count in store:
	            count += 1
	            max_count = max(max_count,count)
	return max_count