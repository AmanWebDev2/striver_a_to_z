def maxDepth(s: str) -> int:
    ans = 0
    open_brackets = 0
    for char in s:
        if char == '(':
            open_brackets += 1
        elif char == ')':
            open_brackets -= 1
        ans = max(open_brackets,ans)
    return ans

print(maxDepth("(1+(2*3)+((8)/4))+1"))