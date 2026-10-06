class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "*-+/":
                stack.append(int(i))
            else:
                if len(stack) >= 2:
                    a, b = stack.pop(), stack.pop()
                    
                    if i == '+':
                        stack.append(b + a)

                    elif i == '-':
                        stack.append(b-a)

                    elif i == '*':
                        stack.append(a*b)

                    else:
                        stack.append(int(b / a))
        return 0 if len(tokens) == 0 else stack[0]