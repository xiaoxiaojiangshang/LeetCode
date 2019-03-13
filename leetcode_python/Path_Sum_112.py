#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/4 22:01   
#  IDE：PyCharm 
import numpy as np



class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None :
            return sum == root.val
        if root.left:
            if self.hasPathSum(root.left,sum - root.val):
                return True
        if root.right:
            if  self.hasPathSum(root.right, sum - root.val):
                return True
        return False
    def pathSum(self, root, sum):
        res,temp = [],[]


if __name__ == '__main__':
    sum = 22


