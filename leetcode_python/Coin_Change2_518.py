# -*- ecoding: utf-8 -*-
# ModuleName: Coin_Change2_518
# IDE:PyCharm
# Author: David
# Time: 2022-03-15 00:24
from typing import List
"""
假设dp[i] 代表组成i 的硬币最少组合，那coins = [1,5] dp[6] = dp[1] + dp[5]?
不太对，那么假设dp[i][j] 代表 前j 个硬币，保持有序
那么1,5 或者5,1 就不会重复
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i - coin]
            # for i in range(1, amount+1):
            #     if i >= coin:
            #         dp[i] += dp[i-coin]
        return dp[amount]
    ## 可以优化一下




def main_test():
    amount = 5
    coins = [1, 2, 5]
    sl = Solution()
    print(sl.change(amount,coins))

if __name__ == '__main__':
    main_test()