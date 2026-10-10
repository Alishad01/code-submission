class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if len(stack) > 0: 
                if i < 0 and stack[-1] > 0:
                    a, b = stack.pop(), i 
                    if abs(a) != abs(b):
                        maxi = a if abs(a) > abs(b) else b
                        stack.append(maxi)
                    continue
            stack.append(i)
        return stack