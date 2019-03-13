#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/2 19:44   
#  IDE：PyCharm 

import numpy as np

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = {}
        begin, end, count, s_len, min_begin, dist = 0, 0, len(t), len(s), 0, len(s)+1
        for i in t:
            if i not in map:
                map[i] = 1
            else: map[i] += 1
        while end < s_len :
            if s[end] in map: ## 符合要找的字符串
                if map[s[end]] > 0: ##还没出现过
                    count -= 1
                map[s[end]] -= 1

            while count == 0:  # 相等就
                if end - begin < dist:
                    min_begin = begin
                    dist = end - begin +1
                if s[begin] in map:
                    map[s[begin]] += 1
                    if map[s[begin]] == 1: ## 符合要找的字符串
                        count += 1
                begin += 1
            end += 1
        return s[min_begin:min_begin+dist] if dist < len(s)+1 else ""

if __name__ == '__main__':
    S = "ADOBECCODEBANC"
    T = "ABCC"
    print("The answer is %s" % (Solution().minWindow(S, T)))