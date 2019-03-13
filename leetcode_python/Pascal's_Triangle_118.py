#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/8 18:54   
#  IDE：PyCharm 
import numpy as np


## it maybe a easy question ,but it is a brilliant solution,i like it
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for _ in range(1,numRows):
            res.append(list(map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1])))
        return res
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return []
        res = [1]
        for _ in range(rowIndex):
            res = list(map(lambda x, y: x+y, res+[0], [0]+res))
        return res

if __name__ == '__main__':
    print(Solution().getRow(0))
