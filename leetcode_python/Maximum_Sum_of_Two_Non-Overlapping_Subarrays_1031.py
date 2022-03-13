# -*- ecoding: utf-8 -*-
# ModuleName: Maximum_Sum_of_Two_Non-Overlapping_Subarrays_91031
# IDE:PyCharm
# Author: David
# Time: 2022-03-13 11:35
from typing import List

'''
 solution1:记录一下主要思路 dpm[i] 代表前 i 个元素中 连续m个元素最大和
 显然有 dpm[i] = sum[i,i-1,i-m-1],dpm[i-1] 两个元素最大值 
 一种包含第i 个元素，它等于summ[i] - summ[i-m]
 一种不包含第i 个元素，它等于dpm[i] 
 solution2： 注意到dpm 其实只用了一次，所以某种程度上可以优化
'''

class Solution:
    def maxSumTwoNoOverlap2(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        numsLen = len(nums)
        if numsLen < firstLen + secondLen:
            return -1
        summ = [0]*(numsLen+1)
        for i in range(numsLen):
            summ[i] = summ[i-1] + nums[i]
        dpm, dpn = [0]* numsLen, [0]*numsLen
        dpm[firstLen-1],dpn[secondLen-1] = summ[firstLen-1],summ[secondLen-1]
        for i in range(firstLen,numsLen):
            dpm[i] = max(dpm[i-1],summ[i]-summ[i-firstLen]) ## 注意这里应该是dpm[i-1]
        for i in range(secondLen,numsLen):
            dpn[i] = max(dpn[i-1],summ[i]-summ[i-secondLen])
        answer = 0
        for i in range(firstLen+secondLen-1,numsLen):
            answer = max(answer,summ[i]-summ[i-secondLen]+dpm[i-secondLen])  ## 先firstlen ,然后second len
            answer = max(answer,summ[i]-summ[i-firstLen]+dpn[i-firstLen])
        return answer
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        numsLen = len(nums)
        if numsLen < firstLen + secondLen:
            return -1
        summ = [0] * (numsLen + 1)
        for i in range(numsLen):
            summ[i] = summ[i - 1] + nums[i]
        dpm, dpn = summ[firstLen-1],summ[secondLen-1]
        answer = 0
        for i in range(firstLen + secondLen - 1, numsLen):
            dpm = max(dpm, summ[i-secondLen] - summ[i-secondLen-firstLen])
            answer = max(answer, summ[i]-summ[i-secondLen]+dpm)
            dpn = max(dpn, summ[i - firstLen] - summ[i - secondLen - firstLen])
            answer = max(answer, summ[i] - summ[i - firstLen] + dpn)
        return answer



def main_test():
    nums, firstLen, secondLen = [3,8,1,3,2,1,8,9,0], 2, 3
    print(Solution().maxSumTwoNoOverlap(nums,firstLen,secondLen))

if __name__ == '__main__':
    main_test()