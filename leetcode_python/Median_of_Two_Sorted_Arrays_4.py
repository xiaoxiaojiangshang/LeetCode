# -*- ecoding: utf-8 -*-
# ModuleName: Median_of_Two_Sorted_Arrays_4
# IDE:PyCharm
# Author: 姜贵平
# Time: 2021/7/14 23:37

MIN_NUM = -1e10
MAX_NUM = 1e10

class Solution:
    def findMedianSortedArrays(self, nums1:list, nums2:list):
        m, n = len(nums1),len(nums2) ## 确保第一个遍历的长度小于第二个
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        if n == 0: return 0
        left, right = 0, m
        while left <= right:
            i = (left+right)//2
            j = (m+n+1)//2 - i
            if i>0 and j<n and nums1[i-1] > nums2[j]:
                right = i-1 # i 太大
            elif j>0 and i<m and nums2[j-1] > nums1[i]:
                left = i+1
            else:
                if i == 0: left_max = nums2[j-1]
                elif j == 0: left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1],nums2[j-1])
                if (m+n)%2 == 1: return left_max
                if i == m: right_min = nums2[j]
                elif j == n: right_min = nums1[i] ## 此时i==0且m==n
                else: right_min = min(nums2[j],nums1[i])
                return (left_max+right_min)/2
        return None
    ## second ways:
    def findMedianSortedArrays2(self, nums1: list, nums2: list):
        m, n = len(nums1), len(nums2)  ## 确保第一个遍历的长度小于第二个
        if m > n: return self.findMedianSortedArrays2(nums2, nums1)
        if n == 0: return 0
        left,right = 0,2*m
        while left<=right:
            i = (left+right)//2
            j = m+n -i
            left_l1 = nums1[(i-1)//2] if i!=0 else MIN_NUM
            left_l2 = nums2[(j-1)//2] if j!=0 else MIN_NUM
            right_l1 = nums1[i//2] if i!=2*m else MAX_NUM
            right_l2 = nums2[j // 2] if j != 2*n else MAX_NUM
            if left_l1 > right_l2: right = i - 1
            elif left_l2> right_l1: left = i + 1
            else:
                return (max(left_l1,left_l2)+min(right_l1,right_l2))/2


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [4,5,6]
    sl = Solution()
    print(sl.findMedianSortedArrays2(nums1,nums2))