# -*- ecoding: utf-8 -*-
# ModuleName: Best_Time_to_Buy_and_Sell_Stock IV_188
# IDE:PyCharm
# Author: David
# Time: 2021/7/21 23:38
from typing import List

class Solution:
    def no_limit_profit(self, prices):
        sum = 0
        for index in range(1,len(prices)):
            sum += max(prices[index] - prices[index - 1], 0)
        return sum

    def maxProfit(self, k: int, prices: List[int], free=0) -> int:
        N = len(prices)
        if N < 2: return 0
        if k * 2 + 1 >= N and free == 0: return self.no_limit_profit(prices)
        dp0 = [-prices[0]] * (N+1) ## 代表最后一次是买入
        dp1 = [0] *(N+1) ## 代表最后一次是卖出
        for i in range(1, k+1):
            for j in range(1, N):
                ''' 选择最低买入，最低买入构成，加入在j days, 那么最大为
                 当前最大收益 - 最低价格
                '''
                ## 先买入
                dp0[j] = max(dp0[j-1], dp1[j] - prices[j]) ## 注意到dp1[j] 是上一轮
                ## 后卖出
                dp1[j] = max(dp1[j-1], prices[j] + dp0[j-1]) ## 注意到这是上一轮的价格

        return dp1[N-1]

## 经典
class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ## 还是经典的dp 算法
        N = len(prices)
        if N <= 1: return 0
        buy = [-prices[0]] * N
        sell = [0] * N
        for i in range(1, N):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])  ## i-1 意味着多轮
            sell[i] = max(sell[i - 1], prices[i] - fee + buy[i - 1])
        return sell[N - 1]

if __name__ == '__main__':
    sl = Solution()
    k = 2
    prices = [2,4,1]
    print(sl.maxProfit(k, prices))
