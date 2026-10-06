class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "*-+/":
                stack.append(i)
            else:
                if len(stack) >= 2 and i == '+':
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(a+b)
                elif len(stack) >= 2 and i == '-':
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(a-b)
                elif len(stack) >= 2 and i == '*':
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(a*b)
                else:
                    a, b = int(stack.pop()), int(stack.pop())
                    if b != 0:
                        stack.append(a/b)
                print(i, stack)
        return 0 if len(stack) == 0 else stack[0]