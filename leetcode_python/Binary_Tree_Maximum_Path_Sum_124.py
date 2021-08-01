#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/23 18:56   
#  IDE：PyCharm 
import numpy as np

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def maxPathDown(self,root):
        if not root:
            return 0
        left = max(0, self.maxPathDown(root.left))
        right = max(0, self.maxPathDown(root.right))
        self.max_value = max(self.max_value, root.val+left+right)
        return root.val+max(left, right)

    def maxPathSum(self, root):
        ### 利用self 当做全局变量
        self.max_value = -100000
        self.maxPathDown(root)
        return self.max_value


if __name__ == '__main__':
    input_data = [-10,9,20,15,7]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[2].left = list_node[3]
    list_node[2].right = list_node[4]
    print(Solution().maxPathSum(list_node[0]))
