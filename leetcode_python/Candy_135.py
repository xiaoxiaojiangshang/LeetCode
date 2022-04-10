# -*- ecoding: utf-8 -*-
# ModuleName: Candy_135
# IDE:PyCharm
# Author: David
# Time: 2022-04-10 12:20
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        up = 1
        down = 0
        rat = 1
        peak = 0

        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                rat += up
                peak = up

            elif ratings[i] == ratings[i - 1]:
                down = 0
                peak = 0
                up = 1
                rat += 1

            else:
                down += 1
                up = 1
                rat += down
                if peak <= down: ## 这是顶点的增加，真是一个绝妙的方法
                    rat += 1

        return rat


def main_test():
    sl = Solution()
    ratings = [1,2,3,1,0,-1,-2]
    print(sl.candy(ratings))


if __name__ == '__main__':
    main_test()
