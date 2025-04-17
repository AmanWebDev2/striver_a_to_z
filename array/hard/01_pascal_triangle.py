"""
T.C: O(n^2)
S.C: O(n^2)
"""
def brute(numRows):
    pt = [[1 for _ in range(i+1)] for i in range(numRows)]
    if numRows <= 2:
        return pt
    for i in range(2,len(pt)):
        prev = pt[i-1]
        curr = pt[i]
        for j in range(1,len(prev)):
            curr[j] = prev[j] + prev[j-1]
    return pt

print(brute(5))