#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/19 9:58   
#  IDE：PyCharm 
import numpy as np
# import sys
# sys.setrecursionlimit(10000000)

class Solution(object):
    def two_string_is_equal(self, s1, s2):
        letter = [0]*1024
        # 一种类似于字典技术
        for i in range(len(s1)):
            letter[ord(s1[i])-ord('a')] += 1
            letter[ord(s2[i]) - ord('a')] -= 1
        return any(letter)==False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        # self.two_string_is_equal(s1, s2) == False
        if m != n or sorted(s1) != sorted(s2):
            return False
        if s1 == s2 :
            return True
        for part in range(1,m):
            if (self.isScramble(s1[0:part],s2[0:part])) and (self.isScramble(s1[part:],s2[part:])):
                return True
            if (self.isScramble(s1[0:part], s2[-part:])) and (self.isScramble(s1[part:], s2[0:-part])):
                return True
        return False

class Solution1(object):
    def isScramble(self, s1, s2):
        s1_len, s2_len, interval = len(s1), len(s2), len(s1)
        if s1_len!=s2_len: return False
        if s1_len==0 and s2_len==0: return True
        dp = []
        for i in range(s1_len):
            temp = []
            for j in range(s2_len):
                temp.append([False]*(interval))
            dp.append(temp)
        for inter in range(interval): ## 间隔
            for i_s1 in range(s1_len-inter):
                for j_s2 in range(s2_len-inter):
                    if inter==0:
                        dp[i_s1][j_s2][inter] = (s1[i_s1]==s2[j_s2])
                    part = 0
                    while (dp[i_s1][j_s2][inter]==False) and (part<inter):
                        dp[i_s1][j_s2][inter] = (dp[i_s1][j_s2][part] and dp[i_s1+part+1][j_s2+part+1][inter-part-1]) or \
                                           (dp[i_s1][j_s2+inter-part][part] and dp[i_s1+part+1][j_s2][inter-part-1])
                        if dp[0][0][s1_len - 1]: return True
                        part = part +1
        print(dp)
        return dp[0][0][s1_len-1]


if __name__ == '__main__':
    s1 = ''
    s2 = ''
    print(Solution().isScramble(s1,s2))
    print(Solution1().isScramble(s1,s2))

