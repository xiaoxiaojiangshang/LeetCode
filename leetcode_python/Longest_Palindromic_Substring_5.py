# -*- ecoding: utf-8 -*-
# ModuleName: Longest_Palindromic_Substring_5
# IDE:PyCharm
# Author: David
# Time: 2022-03-22 00:43
from typing import List
'''
solution1:
    常规方法，分成奇偶向两边扩展，这是常规方法，O(n*n),小技巧是将奇偶判定合一，减少代码冗余
    
solution2：
    著名的马拉车算法 参考@https://segmentfault.com/a/1190000008484167 的图
    大概原理是利用最大对称里面的点来减少判断。
    实现有很多技巧，不太容易想到。
    核心：
        if j < r+certer:
        symmetry_i = 2*certer - j
        p[j] = min(p[symmetry_i],r+certer-j)
    技巧：
        防止边界问题，解决奇偶：
            s = "^#" + "#".join(list(s)) + "#$"
'''
class Solution:
    def judge_equal(self, s, left, right):
        s_len = len(s)
        while left > -1 and right < s_len and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    def longestPalindrome(self, s: str) -> str:
        if getattr(self,"longestPalindrome2"):
            return self.longestPalindrome2(s)
        if not s:
            return ''
        answer = s[0]
        for i in range(len(s)): ##如果不从零开始，bb 会出错，
            ##odd
            odd_answer = self.judge_equal(s, i-1, i+1)
            if len(odd_answer) > len(answer):
                answer = odd_answer
            even_answer = self.judge_equal(s, i, i+1)
            if len(even_answer) > len(answer):
                answer = even_answer
        return answer
    ## 实现马拉车算法
    def longestPalindrome2(self, s: str) -> str:
        s = "^#" + "#".join(list(s)) + "#$"
        p = [0] * len(s)
        certer, r, answer = 2, 1, s[2]
        for j in range(3,len(s)-2): ## 前后两个无意义
            if j < r+certer: ##这是防止小于零的数的发生
                i = 2*certer - j ##以center 为中心，j 的左侧对称点
                p[j] = min(p[i],r+certer-j)
            while s[j+p[j]+1] == s[j-p[j]-1]:
                p[j] += 1
            if j+p[j] > r + certer:
                r = p[j]
                certer = j
            if p[j]*2+1 > len(answer):
                answer = s[j-p[j]:j+p[j]+1]
        return answer.replace('#','')

def main_test():
    sl = Solution()
    s = "babad"
    print(sl.longestPalindrome(s))

if __name__ == '__main__':
    main_test()