"""
T.C: O(n^2)
S.C: O(n^2)

Application: 
example 4C2 = 6

go to 4th row and 2nd column
numRows = 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

"""
def apun_ka_brute(numRows):
    pt = [[1 for _ in range(i+1)] for i in range(numRows)]
    if numRows <= 2:
        return pt
    for i in range(2,len(pt)):
        prev = pt[i-1]
        curr = pt[i]
        for j in range(1,len(prev)):
            curr[j] = prev[j] + prev[j-1]
    return pt


def pascal_triangle(numRows):
    triangle = []
    for i in range(numRows):
        rows = [None for _ in range(i+1)]
        rows[0],rows[-1] = 1,1
        for j in range(1,i):
            rows[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(rows)
    return triangle

print(apun_ka_brute(5))
print(pascal_triangle(5))