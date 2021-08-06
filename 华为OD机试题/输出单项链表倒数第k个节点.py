class Node(object):

    def __init__(self, val=0):
        self.val = val
        self.next = None


while True:
    try:
        l, s, k, head = int(input()), list(map(int, input().split())), int(input()), Node()
        print(l,s,k)
        while k:
            head.next = Node(s.pop())
            print(head.next.val)
            head = head.next
            k -= 1
        print(head.val)
    except:
        break