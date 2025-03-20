def reverse(nums,i,j):
	while i < j:
		nums[i],nums[j] = nums[j],nums[i]
		i += 1
		j -= 1

def next_permutation(nums):
	n = len(nums)

	i = n-2

	while i>=0 and nums[i+1] >= nums[i]:
		i -= 1

	if i >= 0:
		j = n-1

		while nums[j] <= nums[i]:
			j -= 1

		nums[i],nums[j] = nums[j],nums[i]

	reverse(nums,i,n-1)

nums = [1,2,3]
next_permutation(nums)
print(nums)