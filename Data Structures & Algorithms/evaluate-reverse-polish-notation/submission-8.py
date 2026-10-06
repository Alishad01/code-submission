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
                        if b != 0 :
                            stack.append(int(b / a))
            print(i, stack)
        return stack[0]