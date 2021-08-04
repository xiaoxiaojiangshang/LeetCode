# -*- ecoding: utf-8 -*-
# ModuleName: House_Robber_337
# IDE:PyCharm
# Author: David
# Time: 2021/8/3 23:52
from typing import List
from common.common_algorithm import Tree
from common.data_structure import TreeNode

class Solution:
    def dfs(self,node):
        if node == None: return [0,0]## 0：包含root最大值，1:不包含root 最大值
        left_parts = self.dfs(node.left)
        right_parts = self.dfs(node.right)

        return [node.val + left_parts[1] + right_parts[1], max(left_parts)+max(right_parts)]
        '''
         这是因为可能会出现一种情况
            1
         2    4
         4
         left_parts = [2,4]
         right_parts =[4,0] -->max == 4+4
        '''


    def rob(self, root: TreeNode) -> int:
        results = self.dfs(node=root)
        return max(results)

if __name__ == '__main__':
    null = None
    tree = Tree()
    input_data = [-10,9,20,null,null,15,7]
    root = tree.build_tree(input_data)
    tree.print_tree()
    print(Solution().rob(root))

