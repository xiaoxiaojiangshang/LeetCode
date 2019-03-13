#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/28 20:42   
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
    def is_two_point(self,left,right):
        if left == None or left == None:
            return left == right
        if left.val != right.val:
            return False
        a = self.is_two_point(left.left, right.right)
        b = self.is_two_point(left.right, right.left)
        return a and b
        # return self.is_two_point(left.left, right.right) and self.is_two_point(left.right,right.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root == None or self.is_two_point(root.left,root.right)

class Solution2(object):
    def is_symmetric_layer_data(self,list):
        list_len = len(list)
        for i in range(int(list_len/2)):
            if list[i] != list[list_len-i-1]:
                return  False
        return True

    def isSymmetric(self, root):
        if root == None:
            return True
        q = queue.Queue()
        q.put(root)
        one_layer_data = []
        num, layer = 0, 0
        while q.empty() == False:
            cur_node = q.get()
            if cur_node == None:
                one_layer_data.append(-10000)
                q.put(None)
                q.put(None)
            else:
                one_layer_data.append(cur_node.val)
                q.put(cur_node.left)
                q.put(cur_node.right)
            num = num +1
            if num == 2**layer:
                if self.is_symmetric_layer_data(one_layer_data) == False:
                    return False
                if sum(one_layer_data) == -10000*len(one_layer_data):
                    return True

                one_layer_data = []
                num, layer = 0, layer+1
        return True


class layer_order(object):
    ## define two queue ,cur ,next.cur: current layer node, next:next layer node
    def two_queue(self,p_root):
        cur, next = queue.Queue(), queue.Queue()
        cur.put(p_root)
        res, layer_list = [], []
        while cur.empty() == False:
            cur_node = cur.get()
            layer_list.append(cur_node.val)
            if cur_node.left:
                next.put(cur_node.left)
            if cur_node.right:
                next.put(cur_node.right)
            if cur.empty():
                cur = next
                next = queue.Queue()
                res.append(layer_list)
                layer_list = []
        return res

    ### 维护三个node，curr，last，nlast，其中，last 是一层最后一个node，nlast是从cur-->last
    ##cur_node = last,即当前节点到达最后一层
    def two_point(self,p_root):
        if p_root == None:
            return []
        cur = queue.Queue()
        cur.put(p_root)
        res, layer_list = [], []
        last, nlast = p_root, None
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
                res.append(layer_list)
                layer_list = []
        return res


if __name__ == '__main__':
    # input_data = [1,2,2,3,4,4,3]
    # input_data = [1,2]
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
    print(Solution().isSymmetric(list_node[0]))
    print(Solution2().isSymmetric(list_node[0]))
    print(layer_order().two_queue(list_node[0]))
    print(layer_order().two_point(list_node[0]))