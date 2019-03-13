#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/27 19:53   
#  IDE：PyCharm 
import numpy as np


class Solution1(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len == 0 or s2_len == 0:
            if s1 + s2 == s3:
                return True
            else: return False
        if s3[-1] == s1[-1] and s3[-1] == s2[-1]:
            return self.isInterleave(s1[:-1],s2,s3[:-1]) or self.isInterleave(s1,s2[:-1],s3[:-1])
        elif s3[-1] == s1[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1])
        elif s3[-1] == s2[-1]:
            return self.isInterleave(s1, s2[:-1], s3[:-1])
        else: return False
#有的正的比较快
class Solution2(object):
    def isInterleave(self, s1, s2, s3):
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len == 0 or s2_len == 0:
            if s1 + s2 == s3:
                return True
            else: return False
        if s3[0] == s1[0] and s3[0] == s2[0]:
            return self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:])
        elif s3[0] == s1[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif s3[0] == s2[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        else: return False
class Solution3(object):
    def isInterleave(self, s1, s2, s3):
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len == 0 or s2_len == 0:
            if s1 + s2 == s3:
                return True
            else: return False
        if s1_len+s2_len != s3_len:
            return False
        ###### table[i][j] reprent s1 [0:i] +s2 [0:j] == s3[0:i+j]
        table = [[False for _ in range(s2_len+1)] for j in range(s1_len+1)]
        for i in range(s1_len+1):
            for j in range(s2_len+1):
                if i == 0 and j == 0:
                    table[i][j] = True ## reprent empty
                elif i == 0:
                    if table[i][j-1] and s2[j-1] == s3[j-1]:
                        table[i][j] = True
                elif j == 0:
                    if table[i-1][j] and s1[i-1] == s3[i-1]:
                        table[i][j] = True
                else:
                    table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
        return table[s1_len][s2_len]
# class Solution4(object):
#     def isInterleave(self, s1, s2, s3):
#         s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
#         if s1_len == 0 or s2_len == 0:
#             if s1 + s2 == s3:
#                 return True
#             else: return False
#         # greedy will lead Reverse order(exp1)
#         count1, count2, count3 = 0, 0, 0
#         while count1<s1_len and count2<s2_len:
#             if s1[count1] == s3[count3]:
#                 count1 += 1
#                 count3 += 1
#                 continue
#             elif s2[count2] == s3[count3]:
#                 count2 += 1
#                 count3 += 1
#             else: return False
#
#         if count1 == s1_len and s2[count2:] == s3[count3:]:
#             return True
#         if count2 == s2_len and s1[count1:] == s3[count3:]:
#             return True
#         return False


if __name__ == '__main__':
    # s1 = "baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab"
    # s2 = "aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb"
    # s3 = "babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab"
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    s1 = 'a'
    s2= 'b'
    s3 = 'a'
    # print(Solution1().isInterleave(s1,s2,s3))
    print(Solution2().isInterleave(s1, s2, s3))
    print(Solution3().isInterleave(s1, s2, s3))
