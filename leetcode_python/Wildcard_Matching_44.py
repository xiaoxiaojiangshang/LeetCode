# -*- ecoding: utf-8 -*-
# ModuleName: Wildcard_Matching_44
# IDE:PyCharm
# Author: David
# Time: 2022-03-20 00:27
from typing import List

'''
这题的动态规划方程不难推导，但是有些细节需要注意一下
dp推导： 
    普通：dp[i][j] = dp[i-1][j-1]
    特殊：* dp[i][j] = dp[i-1][j] or dp[i][j-1]
        dp[i-1][j]  这个相当于当前任意匹配，多个匹配
        dp[i][j-1]  空匹配
边界问题：
    需要考虑一下 p以"*" 开头的情况， 当 s == '' 的时候，不走主流程，就会判断错
    初始化一下
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        dp = [[False]*(p_len+1) for _ in range(s_len+1)]
        dp[0][0] = True
        i = 1
        while i < p_len + 1 and p[i - 1] == '*':
            dp[0][i] = True
            i = i + 1
        for i in range(1, s_len+1):
            for j in range(1, p_len+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]  ##忽略或者零
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[s_len][p_len]

def main_test():
    sl = Solution()
    s, p = "", ""
    print(sl.isMatch(s,p))

if __name__ == '__main__':
    main_test()