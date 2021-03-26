class Stack:
    def __init__(self):
        self._lst = [ ]
    def push(self, item):
        """入栈"""
        self._lst.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if not self.is_empty():
            return self._lst.pop()

    def peek(self):
        if self._lst:
            return self._lst[-1]
        else:
            return None

    def is_empty(self):
        return self._lst == [ ]

    def size(self):
        return len(self._lst)


if __name__ == '__main__':
    s = Stack()

    for i in range(5):
        s.push(i)
    while s.size():
        print(s.pop())