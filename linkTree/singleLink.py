class LinkNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList:
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur:
            data = cur.item
            print(data, end=" ")
            cur = cur.next

    def add(self, data):
        node = LinkNode(data)
        node.next = self._head
        self._head = node

    def append(self, data):
        node = LinkNode(data)
        cur = self._head
        if self.is_empty():
            self._head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

if __name__ == '__main__':
    link = SingleLinkList()
    print(link.is_empty())
    print(link.length())

    for i in range(5):
        link.append(i)
    print(link.travel())
    print(link.length())