class Stack:
    """КРАЇЛО КРАСАВЧИК"""
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0

class MyQueue:
    """КРАЇЛО КРАСАВЧИК"""
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()
