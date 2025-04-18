"""
Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""
def brute(nums1, nums2):
    arr = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j += 1

    while i < len(nums1):
        arr.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        arr.append(nums2[j])
        j += 1
    
    l = 0
    r = len(arr)-1
    mid = l + (r-l) // 2
    if len(arr) % 2 == 0:
        return (arr[mid] + arr[mid+1]) / 2
    return arr[mid]

"""
Time Complexity: O((n+m)log(n+m))
Space Complexity: O(n+m)
"""
def approach_1(nums1, nums2):
    arr = sorted(nums1 + nums2) # O(n+m) plus sorting O((n+m)log(n+m))
    l = 0
    r = len(arr)-1
    mid = l + (r-l) // 2
    if len(arr) % 2 == 0:
        return (arr[mid] + arr[mid+1]) / 2
    return arr[mid]

print(brute([1, 3], [2]))
print(approach_1([1, 3], [2]))
print(approach_1([1, 2], [3, 4]))
print(approach_1([0, 0], [0, 0]))
print(approach_1([], [1]))
print(approach_1([2], []))
