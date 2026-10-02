class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in operations:
            if i == 'D':
                arr.append((arr[-1]*2))
            elif i == 'C':
                arr.pop()
            elif i == '+':
                # a, b = arr.pop(), arr.pop()
                arr.append((arr[-1]+arr[-2]))
            else:
                arr.append(int(i))
        return sum(arr)