def brute(nums,t):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += nums[k]
            if sum == t:
                count += 1
    return count

def better_brute(nums,t):
    n = len(nums)
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            
            if sum == t:
                count += 1
             
    return count

def optimal(nums,t):
    mpp = set()
    mpp.add(0)
    count = 0
    for num in nums:
        rem = t - num
        if rem in mpp:
            count += 1
        else:
            mpp.add(num)
    return count

