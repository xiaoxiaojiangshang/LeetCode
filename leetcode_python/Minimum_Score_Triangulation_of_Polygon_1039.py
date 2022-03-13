# -*- ecoding: utf-8 -*-
# ModuleName: Minimum_Score_Triangulation_of_Polygon_1039
# IDE:PyCharm
# Author: David
# Time: 2022-03-14 00:01
from typing import List
"""
动态规划： 定义dp[i][j] i 到 j 最小值
dp[i][j] = min(dp[i][k] + dp[k][j] +a[i]*a[k]*a[j]
k 代表我们选中的一个点
"""

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        if n < 2:
            return 0
        dp = [[0]*n for _ in range(n)] ## a tricky, < 2 的为零，大于的为一个大数
        for step in range(2,n):
            for i in range(n-step):
                j = i + step
                dp[i][j] = 99999999
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j]+values[i]*values[k]*values[j])
        return dp[0][n-1]


def main_test():
    sl = Solution()
    values = [1,2,3]
    print(sl.minScoreTriangulation(values))
if __name__ == '__main__':
    main_test()