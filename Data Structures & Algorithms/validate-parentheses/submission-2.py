class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for i in s:
            if len(seen) > 0:
                if i == ')' and seen[-1] == '(' or i == ']' and seen[-1] == '[' or i == '}' and seen[-1] == '{':
                    seen.pop()
                    continue
            seen.append(i)
        return len(seen) == 0