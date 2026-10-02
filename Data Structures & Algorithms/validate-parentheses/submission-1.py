class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for i in s:
            if i in '([{' :
                seen.append(i)
            elif len(seen) > 0:
                if i == ')' and seen[-1] == '(':
                    seen.pop()
                elif i == ']' and seen[-1] == '[':
                    seen.pop()
                elif i == '}' and seen[-1] == '{':
                    seen.pop()
            else:
                return False
        return len(seen) == 0