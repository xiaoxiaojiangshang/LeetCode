# -*- ecoding: utf-8 -*-
# ModuleName: Maximum_Subarray_Sum_with_One_Deletion_1186
# IDE:PyCharm
# Author: David
# Time: 2022-03-14 01:08
from typing import List

'''
1. 定义一个数据，dp[i] 代表 以i 为结尾的最大值
那么dp[i] = arr[i], dp[i-1] + arr[i]

那么反问： 为什么dp[i] 能代表 到i 的最大值吗？
不能，没办法推导，不具有连续性，比如dp[1] == dp[2],因为 arr[2] 是一个负数，那么显然dp[3]无法获得

2  本题 有两个可能，第一个不删除元素 max(dp)
删除一个j元素， dp[j-1] + 反过来的dp2[j+1]
'''
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return -1
        dp = [0] * n
        for i in range(n):
            dp[i] = max(dp[i-1],0) + arr[i]
        ans = max(dp)
        last = arr[-1]
        for j in range(n-2,0,-1):
            ans = max(ans,dp[j-1] + last)
            last = max(last,0) + arr[j]
        return ans

def main_test():
    sl = Solution()
    arr = [1,-2,-2,3]
    print(sl.maximumSum(arr))

if __name__ == '__main__':
    main_test()