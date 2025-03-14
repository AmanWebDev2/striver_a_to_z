# T.C - O(n^3)
def brute(nums,k):
	n = len(nums)
	size = 0
	for s in range(n):
		for e in range(s,n):
			total = 0
			for i in range(s,e+1):
				total += nums[i]
			if total == k:
				size = max(size,e-s+1)
	return size

# T.C = O(n^2)
def better_brute(nums,k):
	n = len(nums)
	size = 0
	for i in range(n):
		total = 0
		for j in range(i,n):
			total += nums[j]
			if total == k:
				size = max(size,j-i+1)
	return size

def better(nums,k):
	n = len(nums)
	size = 0
	total = 0
	mpp = dict()
	for i in range(n):
		total += nums[i]
		if total == k:
			size = max(size,i+1)

		rem = total - k
		if rem in mpp:
			size = max(size,i-mpp.get(rem))

		if total not in mpp:
			mpp[total] = i
	return size



arr = [1,1,1,1,1,1]
# print(brute(arr,4))
print(better(arr,4))
