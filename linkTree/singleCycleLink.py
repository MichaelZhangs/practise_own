class LinkNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList:
    #单向循环链表
    def __init__(self, node=None):
        self._head = node
        if node:
            print("---->", node.elem)
            node.next = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        if self.is_empty():
            return
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            data = cur.item
            print(data, end=" ")
            cur = cur.next
        #退出
        print(cur.item, end=" ")

    def add(self, data):
        node = LinkNode(data)
        cur = self._head
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = self._head

    def append(self, data):
        node = LinkNode(data)
        cur = self._head
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            while cur.next != self._head:
                cur = cur.next
            #方式一
            # node.next = cur.next
            # cur.next = node
            #方式二
            cur.next = node
            node.next = self._head

    def insert(self, pos, data):
        if pos <= 0:
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            pre = self._head
            count = 0
            while count < pos -1:
                count += 1
                pre = pre.next
            node = LinkNode(data)
            node.next = pre.next
            pre.next = node

    def is_exist(self, data):
        if self.is_empty():
            return False

        cur = self._head
        while cur.next != self._head:
            if cur.item == data:
                return True
            cur = cur.next
        #退出循环，判断尾节点
        if cur.item == data:
            return True
        return False

    def remove(self, data):
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.item == data:
                #找到节点
                #头节点
                if cur == self._head:
                    #头节点
                    #找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    #中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #退出循环，尾节点
        if cur.item == data:
            if cur == self._head:
                #只有一个节点
                 self._head = None
            else:
                pre.next = cur.next


if __name__ == '__main__':
    link = SingleLinkList()
    print(link.is_empty())
    print(link.length())

    for i in range(5):
        link.append(i)
    link.travel()

    print()
    print(link.length())
    link.insert(3,10)
    print(link.length())
    link.travel()
    print()
    print(link.is_exist(4))
    link.remove(0)
    print("=========")
    link.travel()
