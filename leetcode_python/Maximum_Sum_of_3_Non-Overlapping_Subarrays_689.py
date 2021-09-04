# -*- ecoding: utf-8 -*-
# ModuleName: Maximum_Sum_of_3_Non-Overlapping_Subarrays_689
# IDE:PyCharm
# Author: David
# Time: 2021/8/24 1:04
from typing import List
from common.common_algorithm import Tree
from common.data_structure import TreeNode

class Solution:
    '''
    dp[i][j] 代表i,j 最大的k 值
    这是一个o(n*n) 的方案，可以有所优化
    '''
    def maxSumOfThreeSubarrays_1(self, nums: List[int], k: int) -> List[int]:
        ## dp[i][j] 代表 i,j 范围内k 个元素最大值,索引
        n = len(nums)
        sum_temp = [0] * (n+1)
        for i in range(1,n+1):
            sum_temp[i] = nums[i-1] + sum_temp[i-1]
        ## dp[i][j] 代表 i..j-1 k 个元素最大值
        dp = [[0] *(n+1) for _ in range(n+1)]
        ## path[i][j] 代表i..j-1 k 个元素最大值的起始位置
        path = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-k+1): ## max(i) = n-k
            dp[i][i+k] = sum_temp[i+k] - sum_temp[i]
            path[i][i+k] = i
            for j in range(i+k+1,n+1):
                k_temp = sum_temp[j] - sum_temp[j-k]
                if k_temp>dp[i][j-1]:
                    dp[i][j] = k_temp
                    path[i][j] = j-k
                else:
                    dp[i][j] = dp[i][j-1]
                    path[i][j]= path[i][j - 1]
        ans,max_result = [0,0,0],0
        for first_index in range(k,n-2*k+1):
            for seconde_index in range(first_index+k,n-k+1):
                sum_temp = dp[0][first_index] + dp[first_index][seconde_index] + dp[seconde_index][n]
                if max_result<sum_temp:
                    ans = [path[0][first_index],path[first_index][seconde_index],path[seconde_index][n]]
                    max_result = sum_temp
        return ans
    '''
    换个思路，本题目中三个区间，可以将中间一个固定，分为[0,i-1],[i,i+k-1],[i+k,n-1]
    那么我们只需要求left:[0,i] 最大值，right:i+k,n-1 最大值
    对于left: 从左到右遍历一遍就可以获得了
    '''
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ## dp[i][j] 代表 i,j 范围内k 个元素最大值,索引
        n = len(nums)
        sum_temp = [0] * (n+1)
        for i in range(1,n+1):
            sum_temp[i] = nums[i-1] + sum_temp[i-1]
        pre = [0] *n
        max_sum_k_temp = sum_temp[k] - sum_temp[0]
        for i in range(k,n-2*k):
            sum_k_temp = sum_temp[i+1] - sum_temp[i+1-k]
            if sum_k_temp>max_sum_k_temp:
                max_sum_k_temp = sum_k_temp
                pre[i] = i+1-k
            else:
                pre[i] = pre[i-1]
        last = [n-k] *n # 存放最后一行最大索引
        max_sum_k_temp = sum_temp[n] - sum_temp[n-k]
        for i in range(n-k-1,2*k-1,-1):
            sum_k_temp = sum_temp[i+k] - sum_temp[i]
            if sum_k_temp >= max_sum_k_temp:
                max_sum_k_temp = sum_k_temp
                last[i] = i
            else:
                last[i] = last[i+1]
        ans = [0,k,2*k]
        max_sum_3k_temp = sum_temp[3*k] - sum_temp[0]
        ## second_index: k..n-2*k
        for i in range(k,n-2*k+1):
            pre_index = pre[i-1]
            pre_k_sum = sum_temp[pre_index+k] - sum_temp[pre_index]
            last_index = last[i+k]
            last_k_sum = sum_temp[last_index+k] - sum_temp[last_index]
            mid_k_sum = sum_temp[i+k] - sum_temp[i]
            if pre_k_sum + mid_k_sum + last_k_sum>max_sum_3k_temp:
                ans = [pre_index, i, last_index]
                max_sum_3k_temp = pre_k_sum + mid_k_sum + last_k_sum
                print(pre_k_sum,mid_k_sum,last_k_sum)
        return ans

if __name__ == '__main__':
    nums = [7,13,20,19,19,2,10,1,1,19]
    k = 3
    print(Solution().maxSumOfThreeSubarrays(nums,k))
