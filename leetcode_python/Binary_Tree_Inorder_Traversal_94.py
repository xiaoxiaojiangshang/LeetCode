#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/24 15:55   
#  IDE：PyCharm 
import numpy as np


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def recursive(self,root,inorder_traversal):
        if root.left:
            self.recursive(root.left,inorder_traversal)
        inorder_traversal.append(root.val)
        if root.right:
            self.recursive(root.right,inorder_traversal)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_traversal = []
        if root:
            self.recursive(root,inorder_traversal)
        return inorder_traversal

class Solution2(object):# use stack
    def inorderTraversal(self, root):
        inorder_traversal = []
        stack = []
        dict_flag = {}
        if root:
            stack.append(root)
            dict_flag[root] = False
        while stack :
            father= stack.pop()
            if dict_flag[father]:
                inorder_traversal.append(father.val)
            else:
                # stack is oppsite
                if father.right :
                    stack.append(father.right)
                    dict_flag[father.right] = False
                stack.append(father)
                dict_flag[father] = True
                if father.left:
                    stack.append(father.left)
                    dict_flag[father.left] = False
        return inorder_traversal
class Solution3(object):  # use stack
    def inorderTraversal(self, root):
        result, stack = [], [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    result.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return result


C
    input_data = [1, 2, 3, 4]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[2].left = list_node[3]
    inorder_traversal = Solution1().inorderTraversal(list_node[0])
    print(inorder_traversal)
    inorder_traversal = Solution2().inorderTraversal(list_node[0])
    print(inorder_traversal)
