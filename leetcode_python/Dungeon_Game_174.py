# -*- ecoding: utf-8 -*-
# ModuleName: Dungeon_Game_174
# IDE:PyCharm
# Author: David
# Time: 2021/8/2 23:57
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m, n = len(dungeon), len(dungeon[0])
        # for i in range(m):
        #     print(dungeon[i])
        dungeon[m-1][n-1] = -dungeon[m-1][n-1]+1 if dungeon[m-1][n-1]<=0 else min(1,dungeon[m-1][n-1])
        ## 初始化最后一列
        for i in range(m - 2, -1, -1):
            minHp = -dungeon[i][n - 1] + dungeon[i + 1][n - 1]
            dungeon[i][n - 1] = max(minHp,1)
        ## 初始化最后一行
        for j in range(n - 2, -1, -1):
            minHp = -dungeon[m - 1][j] + dungeon[m - 1][j + 1]
            dungeon[m - 1][j] = max(minHp, 1)
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                minHp = -dungeon[i][j] + min(dungeon[i + 1][j], dungeon[i][j + 1])
                dungeon[i][j] = max(minHp, 1)
        # for i in range(m):
        #     print(dungeon[i])
        return dungeon[0][0]


if __name__ == '__main__':
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(Solution().calculateMinimumHP(dungeon))