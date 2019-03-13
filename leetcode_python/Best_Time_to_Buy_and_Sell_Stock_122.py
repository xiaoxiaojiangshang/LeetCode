#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/17 21:29   
#  IDE：PyCharm 
import numpy as np


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # while s<e:
        #     if
        # profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(price)):
        #         if prices[j]-prices[i]>profit:
        #             profit = prices[j]-prices[i]
        if not prices:
            return 0
        profit, curr_min = 0, prices[0]
        for price in prices:
            profit = max(price - curr_min, profit)
            curr_min = min(curr_min, price)
        return profit

    def maxProfit1(self, prices):
        if not prices:
            return 0
        profit, pre_price = 0, prices[0]
        for curr_price in prices:
            if pre_price < curr_price:
                profit = profit + curr_price - pre_price
            pre_price = curr_price
        return profit


if __name__ == '__main__':
    prices = [1,2,3,4,5]
    print(Solution().maxProfit1(prices))
