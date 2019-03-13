#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/2 14:09   
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
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
if __name__ == '__main__':
    input_data = [3,4,4,5,5,6,6]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[1].left = list_node[3]
    # list_node[1].right = list_node[4]
    # list_node[2].left = list_node[5]
    list_node[2].right = list_node[4]
    list_node[3].left = list_node[5]
    list_node[4].right = list_node[6]
    print(Solution().maxDepth(list_node[0]))
