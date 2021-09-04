# -*- ecoding: utf-8 -*-
# ModuleName: Elimination_Game_390
# IDE:PyCharm
# Author: David
# Time: 2021/8/15 19:12
from typing import List
from common.common_algorithm import Tree
from common.data_structure import TreeNode
class Solution:
    def lastRemaining(self, n: int) -> int:
        step = 1
        time = 1 ## 记录消除的趟数
        next_first_num = 1
        while n >1:
            if time%2 == 1 or n %2 == 1:
                next_first_num += step
            step = step *2
            time += 1
            n = n//2
        return next_first_num


if __name__ == '__main__':
    a = 10
    print(Solution().lastRemaining(n))