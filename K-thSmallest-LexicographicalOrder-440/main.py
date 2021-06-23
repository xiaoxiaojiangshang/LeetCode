
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans = 1
        k -= 1
        while k > 0:
            gap = self.calculate_nums_gap(ans, ans + 1, n)
            if gap <= k:
                k = k -gap
                ans += 1
            else:
                ans *= 10
                k -= 1
        return ans
    def calculate_nums_gap(self,left_num,right_num,n):
        gap = 0
        while left_num <= n:
            gap += min(n + 1, right_num) - left_num  # max_num:19 == right_num 20
            left_num *= 10
            right_num *= 10
        return gap

if __name__ == '__main__':
    n, k = 1000, 23
    sl = Solution()
    print(sl.findKthNumber(n,k))
    # print(sl.calculate_nums_gap(10,11,1000))