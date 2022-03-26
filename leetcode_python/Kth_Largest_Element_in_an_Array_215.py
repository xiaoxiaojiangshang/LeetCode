# -*- ecoding: utf-8 -*-
# ModuleName: Kth_Largest_Element_in_an_Array_215
# IDE:PyCharm
# Author: David
# Time: 2022-03-23 01:07
from typing import List
from random import randint
""" 
分成两个方法，一个是快排思想，一个是堆排 思想，正好复习一下这两个方法
solution1:
    
solution2:
    
"""
class MySorted:
    def __init__(self, nums=None):
        self.nums = nums if nums else [randint(0,100) for _ in range(50)]
        self.sorted_num = None
        self.count = 0

    def print(self, name="快排"):
        if self.count == 0:
            print("原始的数组为\n", self.nums)
            self.count += 1
        print("经过%s后\n" %name, self.sorted_num)

    """
    quick sort 思想,默认(reversed = False:从小到大)：
        1. 随机找一个数a,返回其索引index，同时保证将[0..index-1] 小于a,[index+1:] 大于a
        2 再分治递归下去
    bug:
        1. 递归一定要有出口，否则会无限递归
        2. low 和 high 需要判断，这个parttion 注意的细节比较多， 重复的bug
    """
    def parttion(self, nums, low, high):
        if low >= high:
            return
        s, e = low, high
        while low < high: ## 显然把第一个数字当做基准
            while low < high and nums[high] > nums[low]:
                high -= 1
            if low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1 ## 重复会有bug
            while low < high and nums[low] < nums[high]:
                low += 1
            if low < high:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1
        self.parttion(nums, s, low - 1)
        self.parttion(nums, low + 1, e)

    def quick_sort(self, nums=None):
        self.sorted_num = nums if nums else list(self.nums)
        low, high = 0, len(self.sorted_num)-1
        self.parttion(self.sorted_num, low, high)
        self.print(name="快排")

    """
    堆排的步骤分成3步骤，建造堆：不断从底向下调整堆的过程。
        技巧：
            2. 堆严格来说将数组当成完全二叉树
            1. 从底向上建造堆， 那么堆的最后一个父母index 是 (n-1)//2 (6,5) -->2
            3 在取数的时候，将最后一个数index=n和堆顶index=0置换，并将调整堆的最大索引设为n(注意是这个n)
    """
    def adjust_heap(self, nums, index, n): ##index 代表索引，完全二叉树, 默认最小堆：输出从大到小
        left, right, min_index = index*2+1, index*2+2, index
        if left < n and nums[min_index] > nums[left]:
            min_index = left
        if right < n and nums[min_index] > nums[right]:
            min_index = right
        if min_index != index: ## 证明调整过
            nums[index], nums[min_index] = nums[min_index], nums[index]
            self.adjust_heap(nums, min_index, n)

    def build_heap(self, nums): ##从底到顶开始调整
        n = len(nums)
        last_index = (n-1)//2
        for i in range(last_index, -1, -1):
            self.adjust_heap(nums, i, n)

    def heap_sort(self, nums=None):
        self.sorted_num = nums if nums else self.nums
        self.build_heap(self.sorted_num)
        for i in range(len(self.sorted_num)-1, 0, -1):
            self.sorted_num[0], self.sorted_num[i] = self.sorted_num[i], self.sorted_num[0]
            self.adjust_heap(self.sorted_num, 0, i)
        self.sorted_num = self.sorted_num[::-1]
        self.print(name="堆排")
    """
    归并排序的思想：分治递归。
        分治：
            二分
            合并
        递归：
            注意判断退出条件
    这与本题无关，只是单独自己想实现一下
    遇到一个小bug:
        i,j = 0,mid+1 这是一个严重bug
    """
    def merge(self, nums, low, high):
        index, temp = 0, [0] * (high-low+1)
        mid = (low + high) // 2
        i, j = low, mid + 1 ##用low 当做赋值的索引吧
        while i < mid+1 and j < high+1:
            if nums[i] <= nums[j]:
                temp[index] = nums[i]
                i += 1
            else:
                temp[index] = nums[j]
                j += 1
            index += 1
        if i == mid+1:
            temp[index:] = nums[j:high+1]
        else:
            temp[index:] = nums[i:mid+1]
        nums[low:high+1] = temp

    def merge_part_sort(self, nums, low, high):
        if low < high:
            mid = (low+high)//2
            self.merge_part_sort(nums, low, mid)
            self.merge_part_sort(nums, mid+1, high)
            self.merge(nums, low, high)
    def merge_sort(self, nums=None):
        self.sorted_num = nums if nums else self.nums
        self.merge_part_sort(self.sorted_num, low=0, high=len(self.sorted_num)-1)
        self.print(name="归并")


class Solution:
    def parttion(self, nums, low, high):
        while low < high:
            while low < high and nums[low] > nums[high]:
                high -= 1
            if low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
            while low < high and nums[low] > nums[high]:
                low += 1
            if low < high:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1
        return low
    """
    快排有个思想，原来的，
        while index != k-1:
            if index > k-1:
                index = self.parttion(nums,low,index-1)
            else:
                index = self.parttion(nums,index+1,high)
        return nums[index]
    点评： low 和high 不变，如果在a,b 之间，那么就有问题
        while index != k - 1:
            if index > k - 1:
                high = index-1
            else:
                low = index + 1
            index = self.parttion(nums, low, high)
        return nums[index]
    思路，就是改变查找区间
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        low, high = 0, len(nums) - 1
        index = self.parttion(nums, low, high)
        while index != k - 1:
            if index > k - 1:
                high = index-1
            else:
                low = index + 1
            index = self.parttion(nums, low, high)
        return nums[index]

def sort_test():
    ms = MySorted()
    ms.quick_sort()
    ms.heap_sort()
    ms.merge_sort()

def main_test():
    sl = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(sl.findKthLargest(nums,k))
if __name__ == '__main__':
    # sort_test()
    main_test()