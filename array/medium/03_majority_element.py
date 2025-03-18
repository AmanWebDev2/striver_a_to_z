# T.C = O(n^2)
def brute(nums):
	n = len(nums)
	for i in range(n):
		count = 0
		for j in range(n):
			if num[i] == nums[j]:
				count += 1
		if count > n // 2:
			return nums[i]
	return -1

# T.C = O(n)
# S.C = O(n)
def better(nums):
	n = len(nums)
	mpp = dict()
	for num in nums:
		mpp[num] = 1 + mpp.get(num,0)

	for num,count in mpp.items():
		if count > n // 2:
			return num
	return -1

# T.C = O(n)
def optimal(nums):
	count = 0
	maj = None
	for num in nums:
		if count == 0:
			maj = num
			count = 0
		elif maj == num:
			count += 1
		else:
			count -= 1
	# 1 step assumption
	# 2 step verification
	# question mai bola hai majority always exist karega
	return maj