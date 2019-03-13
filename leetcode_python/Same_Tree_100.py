#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/28 20:24   
#  IDE：PyCharm 
import numpy as np
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return  True
        if p != None and q!= None:
            if p.val != q.val :
                return False
            if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            return False
        else: return False

if __name__ == '__main__':
    input_data = [1, 2, 3, 4]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[2].left = list_node[3]
    print(Solution().isSameTree(list_node[0],list_node[1]))
