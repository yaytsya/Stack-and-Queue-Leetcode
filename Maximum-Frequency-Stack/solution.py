from collections import deque

class FreqStack:
    """КРАЇЛО КРАСАВЧИК"""
    __slots__ = ['freq', 'group', 'max_freq']

    def __init__(self):
        """КРАЇЛО КРАСАВЧИК"""
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """КРАЇЛО КРАСАВЧИК"""
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        
        if f > self.max_freq:
            self.max_freq = f
            self.group[f] = deque([val])
        else:
            self.group[f].append(val)

    def pop(self) -> int:
        """КРАЇЛО КРАСАВЧИК"""
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        
        if not self.group[self.max_freq]:
            self.max_freq -= 1
            
        return val
