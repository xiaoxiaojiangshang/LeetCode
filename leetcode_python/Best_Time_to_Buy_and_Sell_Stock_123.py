#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/21 22:05   
#  IDE：PyCharm 
import numpy as np


class Solution:
    #time complexity O(k*n) space complexity O(n*2)
    ## 算法的关键是理解 prices[iday]-dp[kth-1][iday-1]
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k, days = 2, len(prices)
        ### dp[k][i] is max_profit of kth,i day;
        dp = [[0 for i in range(days)] for j in range(k+1)]
        for kth in range(1,k+1):
            min_price = prices[0]
            for iday in range(1,days):
                min_price = min(min_price,prices[iday]-dp[kth-1][iday-1])
                dp[kth][iday] = max(dp[kth][iday-1],prices[iday]- min_price)
        return dp[2][days-1]
    #time complexity O(k*n) space complexity O(n)
    ## 交易时间少，小于交易次数可以选这种
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k, days = 2, len(prices)
        ### dp[k][i] is max_profit of kth,i day;
        dp = [0 for i in range(k+1)]
        min_price = [prices[0] for i in range(k+1)]
        for iday in range(1,days):
            for kth in range(1,k+1):
                ## 利用dp[k] 代表第k次交易，到当前填最大收益。
                ## 这是一个可以根据历史推断出现在收益的公式
                min_price[kth] = min(min_price[kth],prices[iday]-dp[kth-1])
                dp[kth] = max(dp[kth],prices[iday]- min_price[kth])
        return dp[2]

    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## 可以选这种交易次数多的
        if not prices:
            return 0
        k, days = 2, len(prices)
        ### dp[k][i] is max_profit of kth,i day;
        ##根据方法一，可推知我们只需要pre，curr两个list维护就行了
        dp = [[0 for i in range(days)] for _ in range(2)]
        for kth in range(1,k+1):
            min_price, pre = prices[0], dp[0]
            for iday in range(1,days):
                min_price = min(min_price,prices[iday]-dp[0][iday-1])
                dp[1][iday] = max(dp[1][iday-1],prices[iday]- min_price)
            dp[0] = list(dp[1])
        return dp[1][days-1]

    def maxProfit4(self, prices):
        if not prices:
            return 0
        buy1, buy2, sell1, sell2 = prices[0], prices[0], 0, 0
        for iday_price in prices:
            buy1 = min(buy1,iday_price);
            sell1 = max(sell1,iday_price - buy1)
            buy2 = min(buy2, iday_price - sell1)
            sell2 = max(sell2, iday_price - buy2)
        return  sell2





if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # prices = [0,3,4]
    print(Solution().maxProfit4(prices))


