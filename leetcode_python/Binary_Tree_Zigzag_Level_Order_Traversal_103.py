#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/2 13:38   
#  IDE：PyCharm 
import numpy as np
import queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        cur = queue.Queue()
        cur.put(root)
        res, layer_list = [], []
        last, nlast, nlayer = root, None, 0
        while cur.empty() == False:
            cur_node = cur.get()
            layer_list.append(cur_node.val)
            if cur_node.left:
                cur.put(cur_node.left)
                nlast = cur_node.left
            if cur_node.right:
                cur.put(cur_node.right)
                nlast = cur_node.right
            if cur_node == last:
                last = nlast
                nlast = None
                if nlayer % 2==1:
                    layer_list.reverse()
                res.append(layer_list)
                nlayer += 1
                layer_list = []
        return res


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
    print(Solution().zigzagLevelOrder(list_node[0]))