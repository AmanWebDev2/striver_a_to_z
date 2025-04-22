
def isBadVersion(version):
    pass

def bruteforce(n):
    for i in range(1, n+1):
        if isBadVersion(i):
            return i

def binary_search(n):
        left = 1
        right = n
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left