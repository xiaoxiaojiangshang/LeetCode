#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/12 19:12   
#  IDE：PyCharm
import numpy as np

class Solution(object):
    # O(n*n)
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left , right, max_area = 0, 0, 0
        for i in range(len(heights)):
            temp = i-1
            while temp >= 0:
                if heights[temp]>=heights[i]:
                    temp -= 1
                else: break
            left = temp
            temp = i+1
            while temp < len(heights):
                if heights[temp]>heights[i]:
                    temp += 1
                else: break
            right = temp
            max_area = max(max_area, heights[i]*(right-left-1))
        return max_area

class Solution1(object):
    # O(n) 并查集的推广
    def largestRectangleArea(self, heights):
        if len(heights) == 0:return 0
        left = np.ones(len(heights)).astype(np.int64)
        right = np.ones(len(heights)).astype(np.int64)
        left[0], right[-1] = -1, len(heights)
        pre, rear , max_area = 0, 0, 0
        for i in range(1,len(heights)):
            pre = i -1
            while pre >= 0:
                if heights[pre] >= heights[i]:
                    pre = left[pre]
                else:
                    break
            left[i] = pre
        for j in range(2,len(heights)+1):
            i = len(heights) -j
            rear = i+1
            while rear < len(heights):
                if heights[rear] >= heights[i]:
                    rear = right[rear]
                else:
                    break
            right[i] = rear
        for i in range(len(heights)):
            max_area = max(max_area, heights[i]*(right[i]-left[i]-1))
        return max_area

class Solution2(object):
    #这个方法，就是寻找一个完全递增的序列，当不满足这个条件的时候，就pop出，满足就push，计算
    # 矩阵面积（因为是递增，所以当前栈中元素，到后一个就是right，栈的前一个元素就是left），
    # 最为机智的在末尾填了一个0，最小数，这样就不用担心中间的小数不能计算了，因为0最小，升序不满足
    # O(n) 维持一个升序序列，这样我们就可以算了
    def largestRectangleArea(self,height):
        height.append(0) # very important trick,
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

if __name__ == '__main__':
    h = [6,2,5,4,5,1,7]
    print("solution1 answer is:",Solution().largestRectangleArea(h))
    print("solution2 answer is:",Solution1().largestRectangleArea(h))
    print("solution3 answer is:", Solution2().largestRectangleArea(h))