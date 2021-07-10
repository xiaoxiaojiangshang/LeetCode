# -*- ecoding: utf-8 -*-
# ModuleName: permutations_46
# IDE:PyCharm
# Author: 姜贵平
# Time: 2021/7/8 23:55


'''
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

import copy
class Solution:
    def __init__(self):
        self.numsLen = -1
        self.ret_list = []

    def backTrack(self,cur,nums):
        if cur==self.numsLen:
                temp = copy.deepcopy(nums)
                self.ret_list.append(temp)
                return
        for i in range(cur,self.numsLen):
            nums[cur],nums[i] = nums[i],nums[cur]
            self.backTrack(cur+1,nums)
            nums[cur], nums[i] = nums[i], nums[cur]

    def permute(self, nums):
        self.numsLen = len(nums)
        self.backTrack(0,nums)
        return self.ret_list
if __name__ == '__main__':
    nums = [1,2,3]
    sl = Solution()
    print(sl.permute(nums))