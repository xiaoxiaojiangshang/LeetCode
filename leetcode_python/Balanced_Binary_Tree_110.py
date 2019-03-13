#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/4 19:16   
#  IDE：PyCharm 
import numpy as np

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0, True
        if root.left == None and root.right == None:
            return 1, True
        left_depth,left_flag = self.maxDepth(root.left)
        right_depth, right_flag = self.maxDepth(root.right)
        if abs(left_depth - right_depth)< 2 and (left_flag and right_flag):
            return max(left_depth,right_depth)+1, True
        else: return 0, False
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return 0
        max_depth, balance_flag = self.maxDepth(root)
        return  max_depth, balance_flag

if __name__ == '__main__':
    input_data = [1,2,3,4,5]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[1].left = list_node[3]
    # # list_node[1].right = list_node[4]
    # # list_node[2].left = list_node[5]
    list_node[2].right = list_node[4]
    # list_node[3].left = list_node[5]
    # list_node[4].right = list_node[6]
    print(Solution().isBalanced(list_node[0]))
    # print(Solution().minDepth(list_node[0]))
