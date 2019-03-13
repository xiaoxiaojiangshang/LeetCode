#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/5 19:55   
#  IDE：PyCharm 

def removeDuplicates(nums):
    count, i = 1, 1
    while i < len(nums):
        if (count == 2) & (nums[i] == nums[i-1]):
            nums.remove(nums[i])
        elif nums[i] == nums[i-1]:
            count += 1
            i +=1
        elif nums[i] != nums[i-1]:
            count = 1
            i += 1
    return nums

class Solution(object):
    def find(self,board,i,j,word):
        # print(board,'\n')
        if len(word) is 0:
            return True
        if i < 0 or j  < 0 or i > len(board) - 1 or j > len(board[0]) - 1:
            return False
        if board[i][j] != word[0]:
            return False
        if word[0] == board[i][j]:
            temp = board[i][j]
            board[i][j] = '?'
            exit_logical = (self.find(board,i-1,j,word[1:]) or self.find(board,i+1,j,word[1:])
                    or self.find(board,i,j-1,word[1:]) or self.find(board,i,j+1,word[1:]))
            board[i][j] = temp
            return exit_logical

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # for i_words in board:
        #     for j_letter in i_words:
        for i_row in range(len(board)):
            for j_col in range(len(board[i_row])):
                if self.find(board,i_row,j_col,word):
                    return True
        return False




if __name__ == '__main__':
    # nums = [1, 1, 1, 2, 2, 3, 3, 3]
    # nums = [0,0,1,1,1,1,2,3,3]
    # print(removeDuplicates(nums))
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']]
    words = ["ABCCED", "SEE", "ABCB"]
    for i_word in words:
        print(Solution().exist(board,i_word))




