#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/22 15:05   
#  IDE：PyCharm

class Solution:
    def conmbain(self,s):
        if  len(s)==0: return 1
        if s[0] == '0': return 0
        if len(s) == 1 :return 1
        if int(s[0:2])<27:
            return self.conmbain(s[1:]) + self.conmbain(s[2:])
        else: return self.conmbain(s[1:])

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre dela
        # s=s.strip('0')
        if len(s)==0:return 0
        if s[0] == '0': return 0
        ret = self.conmbain(s)
        return ret

class Solution2:
    def numDecodings(self, s):
        s_len = len(s)
        if s_len ==0: return 0
        dp = [1] * (s_len + 1)
        if s[s_len-1]=='0':
            dp[s_len-1] = 0
        for i in range(s_len-2,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            elif int(s[i:i+2])<=26:
                dp[i] = dp[i+1] + dp[i+2]
            else:dp[i] = dp[i+1]
        return dp[0]



if __name__ == '__main__':
    str = "475756254584461749104555774581341211511291006816786586787755257741178599337186486723247528324612117156948"
    print(Solution().numDecodings(str))
    print(Solution2().numDecodings(str))
