# -*- ecoding: utf-8 -*-
# ModuleName: Random_Pick_with_Weight_528
# IDE:PyCharm
# Author: David
# Time: 2022-03-16 23:37
from typing import List
import random
import copy

class Solution:
    def binary_search(self):
        left, right = 0,  self.n -1
        num = random.randint(1, self.summ[-1])
        while left <= right:
            middle = (left+right) // 2
            if self.summ[middle]< num:
                left = middle + 1
            elif self.summ[middle]> num:
                right = middle - 1
            else:
                return middle
        return left

    def __init__(self, w: List[int]):
        self.w = w
        self.summ = copy.copy(w)
        for i in range(1,len(w)):
            self.summ[i] += self.summ[i-1]
        self.n = len(w)
    def pickIndex(self) -> int:
        index = self.binary_search()
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

def main_test():
    sl = Solution([1, 3])
    print(sl.pickIndex())
    print(sl.pickIndex())
    print(sl.pickIndex())

if __name__ == '__main__':
    main_test()