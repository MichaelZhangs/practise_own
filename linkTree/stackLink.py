class LinkNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class StackLink:
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

    def pop(self):
        if self.is_empty():
            return
        cur = self.node
        data = cur.item
        cur = cur.next
        self.node = cur
        return data


    def push(self, data):
        node = LinkNode(data)
        if self.is_empty():
            self.node = node
        else:
            node.next = self.node
            self.node = node

    def peek(self):
        """返回头部元素"""
        if self.is_empty():
            return

        cur = self.node
        return cur.item

if __name__ == '__main__':
    link = StackLink()
    print(link.is_empty())
    print(link.size())
    for i in range(5):
        link.push(i)
    print(link.size())
    print(link.pop())
    print("=======")
    print(link.peek())
    print(link.size())
    print("------")
    print(link.pop())
    print(link.peek())




