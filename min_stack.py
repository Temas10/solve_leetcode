class MinStack:

    def __init__(self):
        self.stack = []                    # создаем два стека
        self.stack_min = []                # основной и для миннимальных значений
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_min:                      
            val = min(val, self.stack_min[-1])
        self.stack_min.append(val)

        
    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()