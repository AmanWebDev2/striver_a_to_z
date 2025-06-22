class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(0,len(s),k):
            ans.append(s[i:k+i])

        # fill
        rem = k-len(ans[-1])
        ans[-1] = ans[-1] + fill*rem

        return ans
