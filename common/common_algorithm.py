# -*- ecoding: utf-8 -*-
# ModuleName: common_algorithm
# IDE:PyCharm
# Author: David
# Time: 2021/8/4 23:59
from typing import List
import os
from data_structure import TreeNode
import time

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

def generate_topic(string,root_path='../leetcode_python/'):
    string_list = string.replace('.','').split(' ')
    string_list = string_list[1:] + [string_list[0]]
    file_name = '_'.join(string_list)
    if os.path.exists(root_path+file_name+'.py') == False:
        f = open(root_path+file_name+'.py','w',encoding='utf-8')
        f.write('# -*- ecoding: utf-8 -*-\n')
        f.write('# ModuleName: %s\n'%file_name)
        f.write('# IDE:PyCharm\n# Author: David\n')
        f.write('# Time: {}\n'.format(time.strftime("%Y-%m-%d %H:%M", time.localtime())))
        f.write('from typing import List\nfrom common.common_algorithm import Tree\nfrom common.data_structure import TreeNode\n\n\n\n')
        f.write("if __name__ == '__main__':\n    pass")
        f.close()
    else:
        print("%s file already exits"%file_name)
    return file_name


if __name__ == "__main__":
    string = "943. Find the Shortest Superstring"
    print(generate_topic(string))