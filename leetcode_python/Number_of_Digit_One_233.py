# -*- ecoding: utf-8 -*-
# ModuleName: Number_of_Digit_One_233
# IDE:PyCharm
# Author: David
# Time: 2021/8/5 0:30
from typing import List
from common.common_algorithm import Tree
from common.data_structure import TreeNode


class Solution:
    def to_num(self, string):
        if len(string) == 0: return 0
        return int(string)

    def countDigitOne(self, n: int) -> int:
        n = str(n)
        ret = 0
        for index, num in enumerate(n):
            prefix = self.to_num(n[:index])
            suffix = 10**(len(n)-index-1)
            ret += prefix*suffix
            if num>'1': ret += suffix
            elif num == '1': ret += self.to_num(n[index+1:])+1
        return ret


if __name__ == '__main__':
    a = 100
    print(Solution().countDigitOne(a))