#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/5 10:42   
#  IDE：PyCharm 

import copy

class Solution(object):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    def tracback(self, ret, temp, start, n, k, current):
        if k == current:
            temp_copy = copy.copy(temp)
            ret.append(temp_copy)
            return
        else:
            for i in range(start,n+1):
                temp.append(i)
                self.tracback(ret, temp, i+1, n, k, current+1)
                temp.remove(i)

    def combine(self, n, k):
        ret, temp = [], []
        # for i in range(1, n):
        self.tracback(ret, temp, 1, n, k, 0)
        return ret

if __name__ == '__main__':
    n = 5
    k = 3
    answer = Solution().combine(n,k)
    for i,i_com in enumerate(answer):
        print("第%d组合是" % i, i_com,"\n")