#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/2 14:30   
#  IDE：PyCharm 
import numpy as np
from Binary_Tree_Inorder_Traversal_94 import Solution2 as s2


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree1(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+root_index],inorder[:root_index])
        root.right = self.buildTree(preorder[1+root_index:],inorder[root_index+1:])
        return root

    def buildTree(self, inorder, postorder):
        if len(postorder) == 0 and len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index],postorder[:root_index],)
        root.right = self.buildTree(inorder[1+root_index:],postorder[root_index:-1])
        return root



if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = Solution().buildTree1(preorder,inorder)
    print(s2().inorderTraversal(root))
    root = Solution().buildTree(inorder,postorder)
    print(s2().inorderTraversal(root))
