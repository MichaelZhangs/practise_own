"""
二叉树层序遍历
"""
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        node = [root]
        while(len(node)>0):
            res.append([i.val for i in node])
            node2 = []
            for i in node:
                if i.left:
                    node2.append(i.left)
                if i.right:
                    node2.append(i.right)
            node = node2
        return res