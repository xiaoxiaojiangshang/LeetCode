# -*- ecoding: utf-8 -*-
# ModuleName: Russian_Doll_Envelopes_354
# IDE:PyCharm
# Author: David
# Time: 2021/8/14 1:13
from typing import List
from common.common_algorithm import Tree
from common.data_structure import TreeNode

## 维护一个最大单增序列
class Solution:
    def bianary_search(self,dp,num):
        left,right = 0, len(dp)-1
        while left<=right:
            ## 大于num
            mid = (left+right) // 2
            if dp[mid] >= num: right = mid -1
            else: left = mid +1
        return left
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda k: (k[0], -k[1]))
        envelopes = [x[1] for x in envelopes]
        n = len(envelopes)
        dp = [envelopes[0]] ## dp[i] 代表长度为i的单增字串最后一个数字最小值
        for j in range(1,n):
            index = self.bianary_search(dp,envelopes[j])
            if index == len(dp):dp.append(envelopes[j])
            else:
                dp[index] = envelopes[j]
        return len(dp)

if __name__ == '__main__':
    envelopes =[[1,1],[1,1],[1,1]]
    print(Solution().maxEnvelopes(envelopes))