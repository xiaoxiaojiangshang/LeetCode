#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/2 16:46   
#  IDE：PyCharm 
import numpy as np
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        nums_len = len(nums)
        if nums_len == 0:
            return None
        middle = int(nums_len/2)
        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])
        return root



if __name__ == '__main__':
    nums = [-10,-3,0,5,9]

