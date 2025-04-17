"""
T.C: O(n+m)
S.C: O(n)
"""
def brute(arr,k):
    series = [i for i in range(1,max(arr)+1)]
    count = 0
    for num in series:
        if num not in arr:
            count += 1
        if count == k:
            return num
    return len(arr) + k
    
"""
T.C: O(n)
S.C: O(1)
"""
def better(arr,k):
    i = 0
    n = len(arr)
    num = 0
    while i < n and k > 0:
        num += 1
        # not missing
        if arr[i] == num:
            i += 1
        else:
            k -= 1

    while k > 0:
        num += 1
        k -= 1

    return num

"""
T.C: O(logn)
S.C: O(1)
"""
def optimal(arr,k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k



