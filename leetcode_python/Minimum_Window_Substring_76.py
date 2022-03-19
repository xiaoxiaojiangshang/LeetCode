# -*- ecoding: utf-8 -*-
# ModuleName: Minimum_Window_Substring_76
# IDE:PyCharm
# Author: David
# Time: 2022-03-18 00:20
from typing import List
from collections import defaultdict
'''
method：维持一个滑动窗口来计算最下肢，lefit,right
数据：
need[A] 代表需要A 的个数，显然当所有的需要都小于1，就是满足， 用count 来计数
## 进一步优化，显然我们只需要s 中 在t 中的字符的
当t 特别小的时候，那么 复杂度会降低一丢丢
答案记录：
min_left,min_dist
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = defaultdict(int)
        for letter in t:
            need[letter] += 1
        next_t = []
        for index, letter in enumerate(s):
            if letter in need:
                next_t.append(index)
        if next_t == []: ##这个要注意 next_t 为空的情况
            return ""
        left, min_left, min_dist, count = 0, next_t[0], len(s) + 1, len(t)
        for end in next_t:
            if need[s[end]] > 0: ## 当前字符 是必须的，并非重复
                count -= 1
            need[s[end]] -= 1 ##少一个
            while count == 0: ## 满足条件，left 可以移动
                s_left = next_t[left]
                if end - s_left < min_dist:
                    min_dist = end - s_left + 1
                    min_left = s_left
                need[s[s_left]] += 1
                if need[s[s_left]] >0:
                    count += 1 ## c此时已经不满足
                left += 1
        return s[min_left:min_left+min_dist] if min_dist<=len(s) else ""


def main_test():
    sl = Solution()
    s,t = "B", "A"
    print(sl.minWindow(s,t))


if __name__ == '__main__':
    main_test()