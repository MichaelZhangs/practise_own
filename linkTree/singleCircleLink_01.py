class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Link:
    def __init__(self, node=None):
        self.node = node
        if node:
            node.next = node

    def is_empty(self):
        return self.node == None

    def length(self):
        cur = self.node
        if self.is_empty():
            return
        count = 1
        while cur.next != self.node:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.node
        while cur.next != self.node:
            num = cur.elem
            print(num, end=" ")
            cur = cur.next
        #退出时，最后一个元素
        print(cur.elem, end=" ")


    def add(self, data): #头插法
        node = Node(data)
        cur = self.node
        if self.is_empty():
            self.node = node
            node.next = node
        else:
            while cur.next != self.node:
                cur = cur.next
            node.next = self.node
            self.node = node
            cur.next = self.node

    def append(self, data):
        node = Node(data)
        cur = self.node
        if self.is_empty():
            self.node = node
            node.next = node
        else:
            while cur.next != self.node:
                cur = cur.next
            #方式一
            # cur.next = node
            # node.next = self.node
            #方式二
            node.next = cur.next
            cur.next = node


    def is_exist(self, data):
         if self.is_empty():
             return
         cur = self.node
         while cur.next != self.node:
             num = cur.elem
             if num == data:
                 return True
             cur = cur.next
         #最后一个元素
         if cur.elem == data:
             return True
         return False

    def remove(self, data):
        if self.is_empty():
            return
        if not self.is_exist(data):
            return
        cur = self.node
        pre = None

        #删除头节点
        if cur.elem == data:
            rear = self.node
            while rear.next != self.node:
                rear = rear.next
            rear.next = cur.next
            self.node = cur

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
        if index is None  or index > self.length(): #不指定位置或者位置大于长度
            self.append(data)
        if index is not None:
            if index <= 0:
                self.add(data)
                return
            pre = self.node
            count = 0
            while count < index - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def pop(self):
        #删除最后一个
        if self.is_empty():
            return
        cur = self.node
        while cur.next != self.node:
            pre = cur
            cur = cur.next
        cur.next = self.node
        pre.next = cur.next


if __name__ == '__main__':
    link = Link()
    print(link.is_empty())
    print(link.length())
    for i in range(5):
        link.append(i)
    print("========")
    print(link.is_empty())
    link.travel()
    print()
    print(link.length())
    print(link.is_exist(0))
    link.remove(4)
    link.travel()
    print("========\n")
    link.insert(9)
    link.travel()
    print()
    link.insert(21,5)
    link.travel()
    link.pop()
    print("====")
    link.travel()
