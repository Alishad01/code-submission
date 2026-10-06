class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "*-+/":
                stack.append(int(i))
            else:
                a, b = stack.pop(), stack.pop()
                if len(stack) >= 2 and i == '+':
                    stack.append(a+b)
                elif len(stack) >= 2 and i == '-':
                    stack.append(b-a)
                    
                elif len(stack) >= 2 and i == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(b / a))
            print(i, stack)
        return stack[0]