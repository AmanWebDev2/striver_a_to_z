class Solution:
    # Horizontal Scanning
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
    # Vertical Scanning
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        for i,char in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]