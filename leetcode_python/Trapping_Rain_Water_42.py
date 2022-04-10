# -*- ecoding: utf-8 -*-
# ModuleName: Trapping_Rain_Water_42
# IDE:PyCharm
# Author: David
# Time: 2022-03-31 00:44
from typing import List

class Solution:
    """
    先实现一个简单的算法，求左右两边最大值即可
    answer = min(left[i],right[i])- currHeight
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left_max_height = [0]*n
        for i in range(n):
            left_max_height[i] = max(left_max_height[i-1], height[i])
        right_max, answer = height[-1], 0
        for j in range(n-2,0,-1):
            min_height = min(left_max_height[j], right_max)
            answer += max(0,min_height-height[j])
            right_max = max(right_max, height[j])
        return answer
    ## 用一个单减栈
    """
    这个思路稍微巧妙：
    先思考一个问题：
        一个单减的数据，比如3，2，1
        这个时候来了一个2，比栈顶元素大，那么就会形成沟壑，这个时候就可以计算了
        注意事项：
            如果等于栈顶元素，需要出栈吗，脑海中的图应该是需要的比如：3，2，2，3 --》 (3-2）*(3-0-1)
        这是需要出栈的
            如果栈顶只有一个元素了？两个元素显然形成不了沟壑，不需要计算
    """
    def trap2(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        stack = [0]
        answer = 0
        for i in range(1, len(height)):
            while stack and height[i] >= height[stack[-1]]:
                if len(stack) > 1:
                    pre_index = stack[-2]
                    answer += (min(height[i], height[pre_index]) - height[stack[-1]]) * (i-pre_index-1)
                stack.pop()
            stack.append(i)
        return answer
    """
     双向指针,这个思路比较巧妙，不太容易想，思路2 是水平计算，思路1 和思路3 是垂直算
     双向指针维护左右两边的最大值，如果左边比右边大，右边j 向左更新，反之，左边i 向·右边更新
    """

    def trap3(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        i, j, left_max_height, right_max_height = 1, len(height) - 2, height[0], height[-1]
        answer = 0
        while i <= j:
            if left_max_height >= right_max_height:
                right_max_height = max(right_max_height, height[j])
                answer += right_max_height - height[j]
                j -= 1
            else:
                left_max_height = max(left_max_height, height[i])
                answer += left_max_height - height[i]
                i += 1
        return answer

def main_test():
    sl = Solution()
    height = [4,2,0,3,2,5]
    print(sl.trap(height))
    print(sl.trap2(height))
    print(sl.trap3(height))

if __name__ == '__main__':
    main_test()