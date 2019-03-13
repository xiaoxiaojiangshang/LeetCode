#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/26 10:17   
#  IDE：PyCharm 
import numpy as np

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
## 递归遍历，右边返回最小的，左边最大的
class Solution1(object):
    def isValidBST_left(self, root):
        if root == None:
            return 0, True
        max_left_value, is_left_meet = 0, True
        max_right_value, is_right_meet = 0, True
        if root.left:
            max_left_value, is_left_meet = self.isValidBST_left(root.left)
        if root.right:
            max_right_value, is_right_meet = self.isValidBST_right(root.right)
        if is_left_meet and is_right_meet:
            if max_right_value :
                if root.val>max_left_value and root.val<max_right_value:
                    return max_right_value, True
                else: return 0, False
            elif root.val > max_left_value:
                    return root.val, True
            else: return 0, False
        else:
            return 0, False

    def isValidBST_right(self, root):
        if root == None:
            return 0, True

        max_left_value, is_left_meet = 0, True
        max_right_value, is_right_meet = 0, True
        if root.left:
            max_left_value, is_left_meet = self.isValidBST_left(root.left)
        if root.right:
            max_right_value, is_right_meet = self.isValidBST_right(root.right)
        if is_left_meet and is_right_meet:
            if max_right_value and max_left_value:
                if root.val>max_left_value and root.val<max_right_value:
                    return max_left_value, True
                else: return 0, False
            elif max_right_value and max_left_value==0:
                if root.val < max_right_value:
                    return root.val, True
                else:
                    return 0, False
            elif max_right_value==0 and max_left_value:
                if root.val > max_left_value:
                    return max_left_value, False
                else:
                    return 0, False
            else: return root.val, True
        else:
            return 0, False
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.val == 0 and root.left == None and root.right == None:
            return True
        max_left_value, is_left_meet = 0, True
        max_right_value, is_right_meet = 0, True
        if root.left:
            max_left_value, is_left_meet = self.isValidBST_left(root.left)
        if root.right:
            max_right_value, is_right_meet = self.isValidBST_right(root.right)
        if is_left_meet and is_right_meet:
            if max_right_value:
                if root.val>max_left_value and root.val<max_right_value:
                    return True
                else: return False
            elif root.val > max_left_value:
                    return True
            else:
                return False
        else:
            return False

class Solution2(object):
    def recursive(self,root,inorder_traversal):
        if root.left != None:
            self.recursive(root.left,inorder_traversal)
        inorder_traversal.append(root.val)
        if root.right != None:
            self.recursive(root.right,inorder_traversal)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_traversal = []
        if root:
            self.recursive(root,inorder_traversal)
        num = len(inorder_traversal)
        if num==1 or num==0 :
            return True
        else:
            for i in range(1,num):
                if inorder_traversal[i]<inorder_traversal[i-1]:
                    return False
            return True

if __name__ == '__main__':
    input_data = [5,1,4,3,6]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[2].left = list_node[3]
    list_node[2].right = list_node[4]
    print(Solution1().isValidBST(list_node[0]))
    print(Solution2().isValidBST(list_node[0]))
