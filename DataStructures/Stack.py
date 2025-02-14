class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)