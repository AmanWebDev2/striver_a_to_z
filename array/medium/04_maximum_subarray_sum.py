import math

# T.C = O(n^3)
def brute(nums):
	n = len(nums)
	max_sum = -math.inf
	for i in range(n):
		for j in range(i,n):
			sum = 0
			for k in range(i,j+1):
				sum += nums[k]

			max_sum = max(sum,max_sum)
	return max_sum

# T.C = O(n^2)
def better_brute(nums):
	n = len(nums)
	max_sum = -math.inf
	for i in range(n):
		sum = 0
		for j in range(i,n):
			sum += nums[j]
			max_sum = max(sum,max_sum)
	return max_sum


def optimal(nums):
	n = len(nums)
	max_sum = -math.inf
	sum = 0
	start = -1
	ans_start = -1
	ans_end = -1
	for i,num in enumerate(nums):
		if sum == 0:
			start = i
		sum += num
		if sum > max_sum:
			max_sum = sum
			ans_start = start
			ans_end = i
		if sum < 0:
			sum = 0
	return {"max_sum":max_sum,"ans":nums[ans_start:ans_end+1]}

array = [-2,1,-3,4,-1,2,1,-5,4]
print(optimal(array))