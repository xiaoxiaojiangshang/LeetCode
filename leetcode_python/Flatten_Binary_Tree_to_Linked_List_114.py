#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/7 15:36   
#  IDE：PyCharm 
import numpy as np

class Solution(object):
    def preorder(self,root,res):
        res.append(root)
        if res.left:
            self.preorder(root.left,res)
        if root.right:
            self.preorder(root.right,res)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        if root == None:
            return []
        self.preorder(root,res)
        len_res = len(res)
        if len_res == 1:
            return res
        for i in range(len_res-1):
            res[i].right = res[i+1]
        return res




if __name__ == '__main__':
    print()
