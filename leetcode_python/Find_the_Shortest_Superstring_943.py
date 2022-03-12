# -*- ecoding: utf-8 -*-
# ModuleName: Find_the_Shortest_Superstring_943
# IDE:PyCharm
# Author: David
# Time: 2021-09-05 21:35
from typing import List

## 大致的思路可以参考 https://blog.csdn.net/qq_39559641/article/details/101209534
## 3/12 有一个bug ,最小值的相等的时候路径最小值可能不对，需要记录一下path
## 记录path 引入了一个新的bug ["alex","loves","leetcode"] 没有重合即没有最小的, 这是因为最大值没有超过边界,只需
## 增大1即可
class Solution():
    ## 计算两个单词重复部位,word1 是尾部，word2 是头部
    def calculate_suffix(self,word1,word2):
        word1_len,word2_len = len(word1),len(word2)
        if word1_len < word2_len:
            word2 += (word1_len-word2_len)*'#'
        for i in range(word1_len):
            common_len = len(word1[i:])
            if word1[i:] == word2[:common_len]:
                return common_len, word1 + word2[common_len:].replace('#','')
        return 0, word1 + word2.replace('#','')
    ##  二值化，应该会快一点
    def binary(self,num,words_num):
        binary_list = []
        for i in range(words_num):
            if 2**i & num :
                binary_list.append(i)
        return binary_list
    ## 输出状态记录给出最终结果
    def print_answer(self,last_word_index,path,words):
        status,answer_list = 2**len(words)-1, []
        while last_word_index > -1:
            answer_list.append(last_word_index)
            last_word_index = path[status][last_word_index]
            status = status ^ 2 ** answer_list[-1]
        answer_str = words[answer_list[-1]]
        for i in answer_list[::-1][1:]:
            answer_str = self.calculate_suffix(answer_str,words[i])[1]
        return answer_str

    ## dp[i][j] = min(dp[i&2**j][其他位])
    def shortestSuperstring(self, words: List[str]) -> str:
        words_num = len(words)
        staus_num = 2**words_num
        max_combine_len = len(''.join(words)) +1
        dp = [[max_combine_len]*words_num for _ in range(staus_num)]
        path = [[-1]*words_num for _ in range(staus_num)]
        ## init 只有一个的情况
        for i in range(words_num):
            dp[2**i][i] = len(words[i])
        for i in range(1,staus_num):
            ## 如果二进制中第j 位置事零，那代表i&2**j == 0
            binary_list = self.binary(i,words_num)
            for curr_end_index in binary_list:
                for pre_end_index in binary_list:
                    if pre_end_index == curr_end_index:
                        continue
                    increse_lengh = len(words[curr_end_index]) - self.calculate_suffix(words[pre_end_index],words[curr_end_index])[0]
                    if dp[i][curr_end_index] > dp[i^2**curr_end_index][pre_end_index] + increse_lengh:
                        dp[i][curr_end_index] = dp[i^2**curr_end_index][pre_end_index] + increse_lengh
                        path[i][curr_end_index] = pre_end_index ## 记录一下上个路径
        last_word_index, min_len = 0, dp[staus_num-1][0]
        for i in range(1,len(words)):
            if dp[staus_num-1][i] < min_len:
                last_word_index = i
                min_len = dp[staus_num-1][i]
        return self.print_answer(last_word_index,path,words)

def main_test():
    words = ["wmiy","yarn","rnnwc","arnnw","wcj"]
    # answer = "gctaagttcatgcatc"
    # words = ["alex", "loves", "leetcode"]
    # words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    sl = Solution()
    print(sl.shortestSuperstring(words))
    # print(sl.shortestSuperstring(words) == answer)
    print(sl.calculate_suffix("yarnnwmiy",'rnnwcj'))

if __name__ == '__main__':
    main_test()
