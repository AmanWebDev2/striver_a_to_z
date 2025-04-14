"""
    Time Complexity: O(n * log(max(bloomDay)))
    Space Complexity: O(1)
"""
def binary_search(bloomDay,m,k):
    l = 1
    r = max(bloomDay)
    ans = -1
    def getDays(d):
        cf = 0
        cb = 0
        for days in bloomDay:
            # print(cb,cf)
            if cb == m:
                return True
            if d >= days:
                cf += 1
                if cf == k:
                    cb += 1
                    cf = 0
            else:
                cf = 0
        # print(cb,d)
        return cb == m


    while l <= r:
        mid = (l+r) // 2

        days = getDays(mid)
        # print(days)
        if days:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

print(binary_search([1,10,3,10,2],3,1))