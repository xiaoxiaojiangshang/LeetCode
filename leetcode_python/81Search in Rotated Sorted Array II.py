#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/11 18:57   
#  IDE：PyCharm 

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        ## 三种情况，知道在左边，知道在右边，不知道左边还是右边
        left, right, mid = 0, len(nums)-1, 0
        while left <= right :
            mid = int((left+right)/2)
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                left += 1
                continue
            ## 判断一下有序否
            if nums[left] < nums[mid] : ##左边有序
                if (nums[left] <= target) &(nums[mid]>target):#只有target小于时候不确定
                    right = mid -1
                else: left = mid +1 ## target 大于mid，因为左边有序，只能在右边了。
            else:
                if (nums[mid]<target) & (nums[right]>=target): #右边有序
                    left = mid + 1
                else:
                    right = mid - 1
        return False

if __name__ == '__main__':
    nums = [1,3,5]
    target = 1
    print(Solution().search(nums,target))