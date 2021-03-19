class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Link:
    def __init__(self, node=None):
        self.node = node

    def is_empty(self):
        return self.node == None

    def length(self):
        cur = self.node
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.node
        while cur:
            num = cur.elem
            print(num, end=" ")
            cur = cur.next


    def add(self, data): #头插法
        node = Node(data)
        if self.is_empty():
            self.node = node
        else:
            node.next = self.node
            self.node = node

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.node = node
        else:
            cur = self.node
            while cur.next:
                cur = cur.next
            cur.next = node

    def is_exist(self, data):
         if self.is_empty():
             return
         cur = self.node
         while cur:
             num = cur.elem
             if num == data:
                 return True
             cur = cur.next
         return False

    def remove(self, data):
        if self.is_empty():
            return
        if not self.is_exist(data):
            return
        cur = self.node
        pre = None
        while cur:
            if cur.elem != data:
                pre = cur
                cur = cur.next
            else:
                if cur == self.node:
                    self.node = cur.next
                    break
                else:
                    pre.next = cur.next
                    break

    def insert(self, data, index= None):
        #index 指定插入位置
        node = Node(data)
        if self.is_empty():
            self.add(data)
        cur = self.node
        count = 0
        pre = None
        if index is None: #不指定位置，默认追加
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            if index > self.length(): #索引超过长度，默认追加
                self.append(data)
                return
            if index <= 1:
                self.add(data)
            else:
                while cur:
                    count += 1
                    if count != index:
                        pre = cur
                    else:
                        pre.next = node
                        node.next = cur
                    cur = cur.next

    def pop(self):
        #删除最后一个
        if self.is_empty():
            return
        cur = self.node
        while cur:
            pre = cur
            cur = cur.next
        self.remove(pre.elem)

    def reverse(self, head):
        head = self.node
        if self.is_empty():
            return
        if self.length() == 1:
            return
        pre = None #构造的节点
        while head:
            temp = head.next  #零时变量，保存断开的节点
            head.next = pre
            pre = head
            head = temp

        while pre:
            print(pre.elem, end=" ")
            pre = pre.next

if __name__ == '__main__':
    link = Link()
    print(link.is_empty())
    print(link.length())
    for i in range(5):
        link.append(i)
    print("========")
    print(link.is_empty())
    print(link.remove(0))
    link.insert(9)
    link.insert(-1,0)
    print(link.length())
    print(link.travel())
    link.insert(10, 7)
    link.insert(22 ,1)
    link.travel()
    print()
    link.pop()
    link.travel()
    print()
    print("--------")
    link.reverse(link.node)