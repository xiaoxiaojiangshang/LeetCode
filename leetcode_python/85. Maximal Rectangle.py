#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/13 20:55   
#  IDE：PyCharm 

class Solution(object):
    #维持一个递增序列
    def largest_rectangle(self,height):
        max_area = 0
        height.append(0)
        stack =[-1]
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] -1
                max_area = max(max_area,h*w)
            stack.append(i)
        return max_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        height = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i_col in range(len(matrix[0])):
            if matrix[0][i_col] is '1':
                height[0][i_col] = 1
            for j_row in range(1,len(matrix)):
                if matrix[j_row][i_col] is '1':
                    height[j_row][i_col] = height[j_row-1][i_col] +1
        max_rectangle = 0
        for i_height in height:
            max_rectangle = max(max_rectangle,self.largest_rectangle(i_height))
        return max_rectangle


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalRectangle(matrix))