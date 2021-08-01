#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/12/12 10:38   
#  IDE：PyCharm
class Solution:
    def numDistinct1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_len, t_len = len(s), len(t)
        if t_len == 0:
            return 1
        dp = [[0 for _ in range(t_len+1)] for j in range(s_len+1)]
        for i in range(s_len+1):
            dp[i][0] = 1
        for i in range(1,s_len+1):
            for j in range(1,t_len+1):
                try:
                    if s[i-1] == t[j-1]: ## 保留s[i],或者 去掉s[i]
                        dp [i][j] = dp[i-1][j-1] +dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
                except:
                    print(i,j)
        return dp[s_len][t_len]

    def numDistinct(self, s, t):
        def dfs(s,t):
            s_len, t_len = len(s), len(t)
            if s_len<t_len: return 0
            if t_len == 0: return 1
            if s_len == 0: return 0
            res = dfs(s[1:],t)
            if s[0] == t[0]: res += dfs(s[1:],t[1:])
            return res
        ret = dfs(s,t)
        return ret

if __name__ == '__main__':
    S = "rabbbit"
    T = "rabbit"
    print(Solution().numDistinct(S,T))
