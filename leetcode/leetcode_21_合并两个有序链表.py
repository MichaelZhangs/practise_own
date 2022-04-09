"""
将两个升序链表合并为一个新的 升序 链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeList(self, List1:Optional[ListNode], List2: Optional[ListNode]) -> Optional[ListNode]:
        if not List1:
            return List2
        if not List2:
            return List1
        if List1.val < List2.val:
            List1.next = self.mergeList(List1.next, List2)
            return List1
        else:
            List2.next = self.mergeList(List2.next, List1)
            return List2
if __name__ == '__main__':
    lst1 = ListNode()
    lst2 = ListNode()
    for i in [1,2,4]:
        a = ListNode(i)
        lst1.next = ListNode(i, a)
    for i in [1,3,4]:
        b = ListNode(i)
        lst2.next = ListNode(i, b)
    lst = Solution().mergeList(lst1, lst2)
    while lst:
        print(lst.val)
        lst = lst.next
