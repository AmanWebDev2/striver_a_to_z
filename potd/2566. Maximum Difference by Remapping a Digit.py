"""
    most significant postion from right to left
    least significant position from left to right
    number of digits - O(log(n)) base 10

    T.C - O(logn)
    S.C - O(logn)
"""

class Solution:
    def minMaxDifference(self, num: int) -> int:
        mini = str(num)
        mini = mini.replace(mini[0],"0")

        maxi = str(num)
        pos = 0
        for i,char in enumerate(maxi):
            if char != "9":
                pos = i
                break
        
        maxi = maxi.replace(maxi[pos],"9")

        return int(maxi) - int(mini)