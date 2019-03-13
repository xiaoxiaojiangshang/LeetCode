#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/5 20:15   
#  IDE：PyCharm


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum,res,temp):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return
        temp.append(root.val)
        if root.left == None and root.right == None :
            if sum == root.val:
                res.append(list(temp))
        if root.left:
            self.hasPathSum(root.left,sum - root.val,res,temp)
        if root.right:
            self.hasPathSum(root.right, sum - root.val,res,temp)
        temp.pop()
        return

    def pathSum(self, root, sum):
        res,temp = [],[]
        self.hasPathSum(root,sum,res,temp)
        return res
if __name__ == '__main__':
    sum = 22
    input_data = [5,4,8,11,13,4,7,2,5,1]
    list_node = []
    for data in input_data:
        list_node.append(TreeNode(data))
    list_node[0].left = list_node[1]
    list_node[0].right = list_node[2]
    list_node[1].left = list_node[3]
    list_node[2].left = list_node[4]
    list_node[2].right = list_node[5]
    list_node[3].left = list_node[6]
    list_node[3].right = list_node[7]
    list_node[5].left = list_node[-2]
    list_node[5].right = list_node[-1]
    print(Solution().pathSum(list_node[0],sum))
