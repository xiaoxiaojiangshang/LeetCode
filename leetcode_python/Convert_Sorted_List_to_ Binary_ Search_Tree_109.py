#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/2 16:45   
#  IDE：PyCharm 
import numpy as np
from Binary_Tree_Inorder_Traversal_94 import Solution2 as s2

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if head == None:
            return
        if head.next == None:
            return TreeNode(head.val)
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

class Solution2():
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

    def sortedListToBST(self, head):
        list_node = []
        while head != None:
            list_node.append(head.val)
            head = head.next
        root = self.sortedArrayToBST(list_node)
if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    list_node = []
    for i in nums:
        list_node.append(ListNode(i))
    for i in range(len(list_node)-1):
        list_node[i].next = list_node[i+1]
    root = Solution().sortedListToBST(list_node[0])
    print(s2().inorderTraversal(root))

