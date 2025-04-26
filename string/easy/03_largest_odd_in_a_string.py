"""
T.C: O(n)
S.C: O(1) 
"""
def largestOddNumber(num: str) -> str:
    for i in range(len(num)-1,-1,-1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""