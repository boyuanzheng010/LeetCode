"""
Implement Stack using Python List
First In Last Out
"""
class MyStack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        temp = self.items.pop(-1)
        return temp

    def top(self) -> int:
        return self.items[-1]

    def empty(self) -> bool:
        temp = (self.items==[])
        return temp

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.items)
obj.push(3)
print(obj.items)
obj.push(6)
print(obj.items)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)

















