#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/22 9:57   
#  IDE：PyCharm 
import numpy as np


class Solution:

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #我的想法是一步步实现，根据规律
        if n == 0: return [0]
        ret = [0,1]
        for i in range(1,n):
            ret_len = len(ret)
            add_num = 2**i
            for j in range(ret_len):
                k = ret_len - 1 - j
                num = ret[k] +add_num
                ret.append(num)
        return ret


if __name__ == '__main__':
    print(Solution().grayCode(2))
    # for i in range(4,1,-1):
    #     print (i)
