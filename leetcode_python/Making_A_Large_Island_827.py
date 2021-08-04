# -*- ecoding: utf-8 -*-
# ModuleName: Making_A_Large_Island_827
# IDE:PyCharm
# Author: David
# Time: 2021/8/2 1:03

from typing import List
from itertools import chain

class Union(object):
    def __init__(self,n):
        self._father = [0] *n
        for i in range(n):
            self._father[i] = i
        self._cnt = [1]*n

    def find(self,x):
        if x != self._father[x]:
            self._father[x] = self.find(self._father[x])
            return self._father[x]
        return x

    def merge(self,x,y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x == father_y:
            return self._cnt[father_x]
        if father_x != father_y:
            self._father[father_y] = father_x
            self._cnt[father_x] += self._cnt[father_y]
        return self._cnt[father_x]



class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ## 这应该是并查集的应用
        try:
            m,n= len(grid), len(grid[0])
        except:
            return 0
        if sum(list(chain(*grid))) == m*n : return m*n
        ui = Union(n*m)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]# 上下左右
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for k in range(4):
                        x,y = i + dx[k], j + dy[k]
                        if x<n and x>-1 and y<n and y>-1 and grid[x][y] == 1:
                            ui.merge(i*n+j, x*n+y)
        max_res = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    candidate_pos = []
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if x<n and x>-1 and y<n and y>-1 and grid[x][y] == 1:
                            flag = True
                            for father in candidate_pos:
                                if ui.find(father) == ui.find(x*n+y):
                                    flag = False
                                    break
                            if flag:candidate_pos.append(x*n+y)
                    sum_temp = 1
                    for pos in candidate_pos:
                        sum_temp += ui._cnt[ui.find(pos)]
                    max_res = max(max_res,sum_temp)
        return max_res

if __name__ == "__main__":
    grid = [[1,1],[1,1]]
    print(Solution().largestIsland(grid))
