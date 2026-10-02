class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in operations:
            if i not in '+CD':
                arr.append(int(i))
            elif i == 'D':
                arr.append((arr[-1]*2))
            elif i == '+':
                arr.append((arr[-1]+arr[-2]))
            else:
                arr.pop()
        return sum(arr)