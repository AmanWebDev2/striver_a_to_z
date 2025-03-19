# T.C = O(n)
# S.C = O(n)
def brute(nums):
	n = len(nums)
	pos = []
	neg = []
	ans = []

	for num in nums:
		if num < 0:
			neg.append(num)
		else:
			pos.append(num)

	for i in range(n//2):
		ans.append(pos[i])
		ans.append(neg[i])

	return ans

# T.C = O(n)
# S.C = O(n)
def approach2(nums):
	n = len(nums)
	ans = [0] * n
	pos = 0
	neg = 1
	for num in nums:
		if num > 0:
			ans[pos] = num
			pos += 2
		else:
			ans[neg] = num
			neg += 2
	return ans