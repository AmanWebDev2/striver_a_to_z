def brute(arr:list[int]):
    n = len(arr)

    temp = []
    
    for num in arr:
        if num != 0:
            temp.append(num)

    for i in range(n):
        if i < len(temp):
            arr[i] = temp[i]
        else:
            arr[i] = 0


def optimal(arr:list[int]):
    j = -1
    for i,num in enumerate(arr):
            if num == 0:
                j = i
                break
        
        if j == -1:
            return
        
        for i in range(j+1,len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j],arr[i]
                j += 1
