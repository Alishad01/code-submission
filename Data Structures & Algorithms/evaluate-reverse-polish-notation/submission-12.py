class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for tok in tokens:
            if tok not in ops:
                stack.append(int(tok))
            else:
                a = stack.pop()
                b = stack.pop()
                if tok == "+":
                    stack.append(b + a)
                elif tok == "-":
                    stack.append(b - a)
                elif tok == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
        return stack[0]