class MyStack:

    def __init__(self):
        self.elf = []

    def push(self, x: int) -> None:
        self.elf.append(x)
        
    def pop(self) -> int:
        return self.elf.pop()

    def top(self) -> int:
        return self.elf[-1]

    def empty(self) -> bool:
        return len(self.elf) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()