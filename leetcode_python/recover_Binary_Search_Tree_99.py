#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/28 9:55   
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
        if root.left != None:
            self.recursive(root.left,inorder_traversal)
        inorder_traversal.append(root.val)
        if root.right != None:
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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        ### 先中序遍历，判断谁错了，再更改过来o(2*n)
        inorder_traversal = self.inorderTraversal(root)
        wrong = []
        inorder_sort = sorted(inorder_traversal)
        for i in range(len(inorder_traversal)):
            if inorder_traversal[i] != inorder_sort[i]:
                wrong.append(inorder_traversal[i])
        result, stack = [], [(root, False)]

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    if cur.val == wrong[0]:
                        cur.val = wrong[1]
                    elif cur.val == wrong[1]:
                        cur.val = wrong[0]
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        inorder_traversal = self.inorderTraversal(root)
        print(inorder_traversal)

if __name__ == '__main__':
    input_data = [1,0]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[2].left = list_node[0]
    list_node[2].right = list_node[3]
    list_node[3].left = list_node[1]
    Solution1().recoverTree(list_node[2])
