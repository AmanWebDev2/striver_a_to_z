# T.C = O(m+n) + O(m+n)
# S.C = O(m + n) + O(m+n)
def brute(arr1,arr2):
    store = set()
    for num in arr1:
        store.add(num)
    for num in arr2:
        store.add(num)
    
    return list(store)

# T.C = O(m+n)
# S.C = O(m+n)
def optimal(arr1,arr2):
    p1 = 0
    p2 = 0
    n1 = len(arr1)
    n2 = len(arr2)
    union = []
    while p1 < n1 and p2 < n2:
        if arr1[p1] <= arr2[p2]:
            if len(union) == 0 or union[-1] != arr1[p1]:
                union.append(arr1[p1])
            p1 += 1
        else:
            if len(union) == 0 or union[-1] != arr2[p2]:
                union.append(arr2[p2])
            p2 += 1

    while p1 < n1:
        if union[-1] != arr1[p1]:
                union.append(arr1[p1])
        p1 += 1

    while p2 < n2:
        if union[-1] != arr2[p2]:
                union.append(arr2[p2])
            p2 += 1
    return union
