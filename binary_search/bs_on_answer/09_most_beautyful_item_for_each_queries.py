def maximumBeauty(items, queries):
    # Sort and store max beauty
    items.sort(key=lambda x: x[0])

    max_beauty = items[0][1]
    for i in range(len(items)):
        max_beauty = max(max_beauty, items[i][1])
        items[i][1] = max_beauty

    return [binary_search(items, q) for q in queries]
    
def binary_search(items, target_price):
    left, right = 0, len(items) - 1
    max_beauty = 0
    while left <= right:
        mid = (left + right) // 2
        if items[mid][0] > target_price:
            right = mid - 1
        else:
            # Found viable price. Keep moving to right
            max_beauty = max(max_beauty, items[mid][1])
            left = mid + 1
    return max_beauty


items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

print(maximumBeauty(items, queries))