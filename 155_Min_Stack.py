class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValueStack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minValueStack) == 0 or x <= self.minValueStack[-1]:
            self.minValueStack.append(x)
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minValueStack[-1]:
            self.minValueStack.pop()
        return x
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValueStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
