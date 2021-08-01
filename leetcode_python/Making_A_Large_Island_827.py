# -*- ecoding: utf-8 -*-
# ModuleName: Making_A_Large_Island_827
# IDE:PyCharm
# Author: David
# Time: 2021/8/2 1:03

class Union(object):
    def __init__(self,N):
        self._father = [0] *N
        for i in range(N):
            self._father[i] = i
        self._cnt = [1]*N

    def find(self,x):
        if x != self._father[x]:
            self._father[x] = self.find(self._father[x])
            return self._father[x]
        return x

    def merge(self,x,y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ## 这应该是并查集的应用
if __name__ == '__main__':
    a = 1