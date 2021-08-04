# -*- ecoding: utf-8 -*-
# ModuleName: common_algorithm
# IDE:PyCharm
# Author: David
# Time: 2021/8/4 23:59
from typing import List
from data_structure import TreeNode
class Tree(object):
    def build_tree(self,input_data):
        n = len(input_data)
        if n == 0:return None
        self.list_node = []

        for data in input_data:
            if data:
                self.list_node.append(TreeNode(data))
            else:
                self.list_node.append(None)
        child_index = 1
        for i in range(n):
            if self.list_node[i] != None:
                try:
                    self.list_node[i].left = self.list_node[child_index]
                    child_index += 1
                    self.list_node[i].right = self.list_node[child_index]
                    child_index += 1
                except:
                    break
        return self.list_node[0]

    def print_tree(self):
        for node in self.list_node:
            if node:
                left = None if node.left == None else node.left.val
                right = None if node.right == None else node.right.val
                print("father:{} | left:{} | right:{}".format(node.val,left,right))

def generate_topic(string):
    string_list = string.replace('.','').split(' ')
    string_list = string_list[1:] + [string_list[0]]
    return '_'.join(string_list)
string = "233. Number of Digit One"
print(generate_topic(string))