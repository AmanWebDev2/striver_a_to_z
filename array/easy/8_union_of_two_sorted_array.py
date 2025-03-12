def brute(a:list[int],b:list[iint]):
    store = set()
    for num in a:
        store.add(num)

    for num in b:
        store.add(num)

    return list(store)


def optimal(a:list[int],b:list[int]):
    i = 0
    j = 0
    m = len(a)
    n = len(b)
    
    temp = []
    
    while i < m and j < n:
        if a[i] <= b[j]:
            if len(temp) == 0 or temp[-1] != a[i]:
                temp.append(a[i])
            i += 1
        else:
            if len(temp) == 0 or temp[-1] != b[j]:
                temp.append(b[j])
            j += 1
            
    while i < m:
        if temp[-1] != a[i]:
                temp.append(a[i])
            i += 1
            
    while j < n:
        if temp[-1] != b[j]:
            temp.append(b[j])
        j += 1 
    return temp
