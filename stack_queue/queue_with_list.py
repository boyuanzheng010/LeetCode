"""
Implement Queue using Python List
First In First Out
"""
class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        temp = self.items.pop(0)
        return temp

    def peek(self) -> int:
        return self.items[0]

    def empty(self) -> bool:
        temp = (self.items==[])
        return temp

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
print(obj.items)
obj.push(6)
print(obj.items)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)











