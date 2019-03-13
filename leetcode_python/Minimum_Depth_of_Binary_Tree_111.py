#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/4 22:01   
#  IDE：PyCharm 
import numpy as np


def minDepth(self, root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    if root.left == None:
        return self.minDepth(root.right) + 1
    elif root.right == None:
        return self.minDepth(root.left) + 1
    else:
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return min(left_depth, right_depth) + 1
if __name__ == '__main__':
    print()
