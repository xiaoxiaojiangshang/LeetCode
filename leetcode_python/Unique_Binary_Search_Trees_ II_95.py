#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/24 20:29   
#  IDE：PyCharm

from Binary_Tree_Inorder_Traversal_94 import Solution as BT
# BST's (binary search trees) ：对于任意的树，左子树的节点<根<右子树的节点
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def catalan(n):
    if n==0 or n==1:
        return 1
    return (4*n-2)*catalan(n-1)/(n+1)
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        memo = {}
        def node(val, left, right):
            root, root.left, root.right = TreeNode(val), left, right
            return root
        def gen(i, j):
            if (i, j) not in memo:
                memo[i, j] = [node(val, left, right)
                    for val in range(i, j + 1)
                    for left in gen(i, val - 1)
                    for right in gen(val + 1, j)] or [None]
            return memo[i, j]
        return gen(1, n)

class Solution1(object):
    def construct_tree(self,start,end):
        for i in range(start,end+1):
            i
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        tree_noed = self.construct_tree(1,n)
        return tree_noed


class Solution2:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                i, start
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        # if len(left_trees)==2 and len(right_trees)==2:
                        #     print(l,r)
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees
        return generate_trees(1, n) if n else []

if __name__ == '__main__':
    n = 1
    tree_node = Solution2().generateTrees(n)
    for node in tree_node:
        print(BT().inorderTraversal(node))

