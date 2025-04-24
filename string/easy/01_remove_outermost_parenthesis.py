def removeOuterParentheses(s: str) -> str:
    stack = []
    ans = ""
    for p in s:
        if p == '(':
            if len(stack) > 0:
                ans += p
            stack.append(p)
        else:
            stack.pop()
            if stack:
                ans += p

    return ans

print(removeOuterParentheses("(()())(())"))