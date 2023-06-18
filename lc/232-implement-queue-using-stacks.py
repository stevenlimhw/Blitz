class MyQueue:

    def __init__(self):
        # invariant#1: right before or after an operation, stack contains
        # the elements and stack_tmp should be empty
        # invariant#2: stack_tmp is only filled (and stack is empty) during operations
        self.stack = []
        self.stack_tmp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        # reverse elements in stack by moving them one by one to stack_tmp
        while self.stack:
            cur = self.stack.pop(-1)
            self.stack_tmp.append(cur)
        # pop the top element in stack_tmp
        res = self.stack_tmp.pop(-1)
        # move the elements back one by one to stack
        while self.stack_tmp:
            cur = self.stack_tmp.pop(-1)
            self.stack.append(cur)
        return res
        

    def peek(self) -> int:
        if not self.stack:
            return -1
        # reverse elements in stack by moving them one by one to stack_tmp
        while self.stack:
            cur = self.stack.pop(-1)
            self.stack_tmp.append(cur)
        # peek the top element in stack_tmp
        res = self.stack_tmp[-1]
        # move the elements back one by one to stack
        while self.stack_tmp:
            cur = self.stack_tmp.pop(-1)
            self.stack.append(cur)
        return res

    # checks whether the data structure is empty
    def empty(self) -> bool:
        res = False
        if not self.stack:
            res = True
        return res


        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()