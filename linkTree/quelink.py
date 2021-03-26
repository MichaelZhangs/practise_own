class LinkNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class QueLink:
    def __init__(self, node=None):
        self.node = node

    def is_empty(self):
        return self.node == None

    def size(self):
        cur = self.node
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def deque(self):
        """删除头部元素"""
        if self.is_empty():
            return
        cur =  self.node
        data = cur.item
        cur = cur.next
        self.node = cur

        return data

    def enque(self, data):
        node = LinkNode(data)
        if self.is_empty():
            self.node = node
        else:
            cur = self.node
            while cur.next:
                cur = cur.next
            cur.next = node

if __name__ == '__main__':
    link = QueLink()
    print(link.is_empty())
    print(link.size())
    for i in range(5):
        link.enque(i)
    print(link.size())
    print("出队 ",link.deque())
    print(link.size())
    print("出队 ", link.deque())
    print(link.size())
    print("出队 ", link.deque())