#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/5 19:11   
#  IDE：PyCharm 
import copy
class Solution(object):
    def tracback(self, ret, temp, nums, cur):
        if cur <= len(nums):
            temp_copy = copy.copy(temp)
            ret.append(temp_copy)
        for i in range(cur,len(nums)):
            temp.append(nums[i])
            self.tracback(ret, temp, nums ,i+1)
            temp.remove(nums[i])

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret ,temp = [],[]
        self.tracback(ret, temp ,nums, 0)
        ## 包含重复的
        return ret
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret ,temp = [],[]
        self.tracback(ret, temp ,nums, 0)
        temp =[]
        for k in ret:
            if k not in temp:
                temp.append(k)
        return temp

if __name__ == '__main__':
    num = [4,4,4,1,4]
    answer = Solution().subsets(num)
    for i,i_com in enumerate(answer):
        print("第%d组合是" % i, i_com,"\n")