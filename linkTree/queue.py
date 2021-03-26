class Queue:
    def __init__(self):
        self._que = [ ]

    def enque(self, data):
        self._que.append(data)

    def deque(self):
        """出队"""
        if not self.is_empty():
            return self._que.pop(0)

    def is_empty(self):
        return self._que == [ ]

    def size(self):
        return len(self._que)

if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        q.enque(i)

    while q.size():
        print(q.deque())