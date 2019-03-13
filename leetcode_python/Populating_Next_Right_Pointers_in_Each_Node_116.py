#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/7 22:05   
#  IDE：PyCharm 
import numpy as np
import copy
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        while root:
            cur = copy.copy(root)
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            root = root.left




if __name__ == '__main__':
    input_data = [1,2,3,4,5,6,7]
    list_node = []
    for data in input_data:
        list_node.append(TreeLinkNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[1].left = list_node[3]
    list_node[1].right = list_node[4]
    list_node[2].left = list_node[5]
    list_node[2].right = list_node[6]
    Solution().connect(list_node[0])
