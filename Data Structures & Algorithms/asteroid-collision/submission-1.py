class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                a = stack.pop()
                if abs(a) > abs(i):
                    stack.append(a)
                    i = 0
                    break
                elif abs(a) == abs(i):
                    i = 0
                    break
             
            if i != 0:
                stack.append(i)
        return stack