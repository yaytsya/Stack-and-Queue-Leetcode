class Queue:
    """КРАЇЛО КРАСАВЧИК"""
    def __init__(self):
        """КРАЇЛО КРАСАВЧИК"""
        self._data = []
        self._head = 0

    def push(self, item):
        """КРАЇЛО КРАСАВЧИК"""
        self._data.append(item)

    def pop(self):
        """КРАЇЛО КРАСАВЧИК"""
        val = self._data[self._head]
        self._head += 1
        return val

    def peek(self):
        """КРАЇЛО КРАСАВЧИК"""
        return self._data[self._head]

    def empty(self):
        """КРАЇЛО КРАСАВЧИК"""
        return self._head >= len(self._data)

    def __len__(self):
        """КРАЇЛО КРАСАВЧИК"""
        return len(self._data) - self._head

class MyStack:
    """КРАЇЛО КРАСАВЧИК"""
    def __init__(self):
        """КРАЇЛО КРАСАВЧИК"""
        self.q = Queue()

    def push(self, x: int) -> None:
        """КРАЇЛО КРАСАВЧИК"""
        self.q.push(x)
        for _ in range(len(self.q) - 1):
            self.q.push(self.q.pop())

    def pop(self) -> int:
        """КРАЇЛО КРАСАВЧИК"""
        return self.q.pop()

    def top(self) -> int:
        """КРАЇЛО КРАСАВЧИК"""
        return self.q.peek()

    def empty(self) -> bool:
        """КРАЇЛО КРАСАВЧИК"""
        return self.q.empty()
