class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for i in s:
            if i in '([{' :
                seen.append(i)
            else:
                if i == ')' and seen[-1] == '(':
                    seen.pop()
                elif i == ']' and seen[-1] == '[':
                    seen.pop()
                elif i == '}' and seen[-1] == '{':
                    seen.pop()
        return len(seen) == 0