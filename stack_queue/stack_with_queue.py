class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        return self.items.pop(0)

    def peek(self) -> int:
        return self.items[0]

    def empty(self) -> bool:
        return self.items == []

    def size(self) -> int:
        return len(self.items)


class MyStack:

    def __init__(self):
        self.queue_1 = MyQueue()
        self.queue_2 = MyQueue()

    def push(self, x: int) -> None:
        self.queue_1.push(x)

    def pop(self) -> int:
        length = self.queue_1.size()
        if length == 1:
            return self.queue_1.pop()
        if length > 1:
            for i in range(length - 1):
                self.queue_2.push(self.queue_1.pop())
            temp = self.queue_1.pop()
            for i in range(length - 1):
                self.queue_1.push(self.queue_2.pop())
            return temp

    # 这里不能简单地取完之后peek，一定要全部取出来
    def top(self) -> int:
        length = self.queue_1.size()
        if length == 1:
            temp = self.queue_1.pop()
            self.queue_1.push(temp)
            return temp
        if length > 1:
            for i in range(length - 1):
                self.queue_2.push(self.queue_1.pop())
            temp = self.queue_1.pop()
            for i in range(length - 1):
                self.queue_1.push(self.queue_2.pop())
            self.queue_1.push(temp)
            return temp

    def empty(self) -> bool:
        return self.queue_1.empty() and self.queue_2.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()