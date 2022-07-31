import os
class Stack:
    """The class implements a stack"""
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        """It returns true if stack is empty otherwise it returns false"""
        return len(self.items)==0
            

    def is_full(self):
        """It returns true if stack is full otherwise it returns false"""
        return len(self.items)==self.size
            

    def push(self, data):
        """It pushes an element to stack if stack is not full"""
        if not self.is_full():
            self.items.append(data)

    def pop(self):
        """It removes an element from stack if stack is not empty"""
        if not self.is_empty():
            self.items.pop(-1)

    def status(self):
        """Displays the stack"""
        for elem in self.items:
            print(elem)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
