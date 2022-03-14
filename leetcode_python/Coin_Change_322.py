# -*- ecoding: utf-8 -*-
# ModuleName: Coin_Change_322
# IDE:PyCharm
# Author: David
# Time: 2022-03-15 00:01
from typing import List

'''
定义一个dp[i] 代表组成 组成i面值的最小组合数
显然dp[i] = min(dp[i],dp[i-coin])
上述解决了一半，但是还有一个问题，如果不能组合怎么办，
比如[2] -->amount = 3
dp[3] = dp[1] 但 dp[1] 应该是个不可到达状态，设置一下最大值，amount +1 吧
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount]<amount+1 else -1


def main_test():
    coins = [2]
    amount = 0
    sl = Solution()
    print(sl.coinChange(coins,amount))

if __name__ == '__main__':
    main_test()