#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/10 21:04   
#  IDE：PyCharm 
import copy
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        temp = copy.copy(root)
        while root:
            cur = copy.copy(root)
            nextTrail = TreeLinkNode(0)
            nextHead = nextTrail
            while cur:
                if cur.left:
                    nextTrail.next = cur.left
                    nextTrail = cur.left
                if cur.right:
                    nextTrail.next = cur.right
                    nextTrail = cur.right
                cur = cur.next
            root = nextHead.next
        return
if __name__ == '__main__':
    input_data = [1,2,3,4,5]
    list_node = []
    for data in input_data:
        list_node.append(TreeLinkNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[1].left = list_node[3]
    list_node[1].right = list_node[4]
    # list_node[2].left = list_node[5]
    # list_node[2].right = list_node[6]
    Solution().connect(list_node[0])
