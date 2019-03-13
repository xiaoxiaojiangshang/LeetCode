#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/13 9:57   
#  IDE：PyCharm 
import numpy as np
class Solution:
    def dfs(self, triangle, sum, min_sum, posi,t_len):
        if posi[0] == t_len-1:
            min_sum = min(sum, min_sum)
            return min_sum
        if sum<min_sum:
            min_sum = self.dfs(triangle,sum + triangle[posi[0]+1][posi[1]+1],min_sum,[posi[0]+1,posi[1]+1],t_len)
            min_sum = self.dfs(triangle,sum+triangle[posi[0]+1][posi[1]],min_sum,[posi[0] + 1, posi[1]],t_len)
        return min_sum

    def minimumTotal(self, triangle):
        t_len = len(triangle)
        if t_len == 0:
            return 0
        sum, min_sum, posi = triangle[0][0], 9999999, [0, 0]
        min_sum = self.dfs(triangle,sum,min_sum,posi,t_len)
        return min_sum
    ## 分析可知，这也可以是个dp问题，逆向思维，如果知道底层到当前层最下的sum，那么上面一层也就知道了
    ## 由底向上
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        for ilayer in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[ilayer])):
                triangle[ilayer][j] = min(triangle[ilayer+1][j],triangle[ilayer+1][j+1]) + triangle[ilayer][j]
        return triangle[0][0]


if __name__ == '__main__':
    triangle = [[-1],[2,3],[1,-1,-1]]
    print(Solution().minimumTotal(triangle))
