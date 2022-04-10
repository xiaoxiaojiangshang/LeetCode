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

    """
    potin: 一个点的得分只与左右两边的点有关系。
    status: up, down, equal
    up: 比前一个大，1,2,3 对于3，需要rating += 3,此时up=3
    down : 与 up 类似，比前一个小，3,2,1，down =3, 但需要注意一下，1,5,4,3,2 中5
    的rating:up=2,down = 4,这个需要技巧来消除结果
    init:
        up, down, ans = 1, 1, 1
    example1:
        2,4,3,2,1   4 的情况下， up=2, down=1. 3 down =2, 
        down = up , down -1
        --> down < up down -1
        --> down >up 2 down =3, 需要加的是3， 这其实是倒过来计算的
    example:
    1,2,2,1 相等的时候重新开始

    error1:
        没有考虑下降后 up 需要等于 1
    error2:
        没有考虑上升后 down = 1
    """

    def candy2(self, ratings: List[int]) -> int:
        up, down, peak, ans = 1, 1, 1, 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                up += 1
                ans += up
                peak = up ## 上升峰顶
                down = 1 ## error 2
            elif ratings[i] == ratings[i-1]:
                up, down = 1, 1
                ans += 1
                peak = 1
            else:
                down += 1
                up = 1 # error1
                ans += [down-1, down][down > peak]
        return ans
def main_test():
    sl = Solution()
    ratings = [5,3,7,3]
    print(sl.candy(ratings))
    print(sl.candy2(ratings))


if __name__ == '__main__':
    main_test()
