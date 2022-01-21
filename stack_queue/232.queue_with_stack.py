class MyStack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        return self.items.pop(-1)

    def peek(self) -> int:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def empty(self) -> bool:
        return self.items == []


class MyQueue:

    def __init__(self):
        self.stack_1 = MyStack()
        self.stack_2 = MyStack()

    def push(self, x: int) -> None:
        self.stack_1.push(x)

    def pop(self) -> int:
        length = self.stack_1.size()
        if length == 1:
            return self.stack_1.pop()
        if length > 1:
            for i in range(length - 1):
                self.stack_2.push(self.stack_1.pop())
            temp = self.stack_1.pop()
            for i in range(length - 1):
                self.stack_1.push(self.stack_2.pop())
        return temp

    def peek(self) -> int:
        length = self.stack_1.size()
        if length == 1:
            return self.stack_1.peek()
        if length > 1:
            for i in range(length - 1):
                self.stack_2.push(self.stack_1.pop())
            temp = self.stack_1.peek()
            for i in range(length - 1):
                self.stack_1.push(self.stack_2.pop())
        return temp

    def empty(self) -> bool:
        return self.stack_1.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()