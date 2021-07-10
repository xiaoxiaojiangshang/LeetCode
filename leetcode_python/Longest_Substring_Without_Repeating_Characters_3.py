# -*- ecoding: utf-8 -*-
# ModuleName: Longest_Substring_Without_Repeating_Characters_3
# IDE:PyCharm
# Author: 姜贵平
# Time: 2021/7/10 23:40

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        max_len = 1
        pos_dict = {}
        cur_len = 0
        for index, letter in enumerate(s):
            if letter not in pos_dict:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = min(cur_len + 1, index - pos_dict[letter])
            pos_dict[letter] = index
        max_len = max(max_len, cur_len)
        return max_len

if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))