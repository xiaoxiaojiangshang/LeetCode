#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/24 13:16   
#  IDE：PyCharm 
import numpy as np

class Solution:
    def conmbain(self, s, count,ip,ip_list):
        if len(s)==0 and len(ip)==4:
            ip_list.append('.'.join(ip))
        if len(ip)>4:
            return
        pos = min(len(s),3)
        for i in range(1,pos+1):
            if (int(s[0:i])>=256) or (s[0]=='0' and i>1):
                continue
            ip.append(s[0:i])
            # count += 1
            self.conmbain(s[i:],count+1,ip,ip_list)
            del ip[-1]


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ip_list, ip, ip_count = [], [], 0
        self.conmbain(s, ip_count, ip, ip_list)
        return ip_list

class Solution1:

    def restoreIpAddresses(self, s):
        s_len = len(s)
        ip_list = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a+b+c+d == s_len:
                            A = int(s[0:a])
                            B = int(s[a:a+b])
                            C = int(s[a+b:a+b+c])
                            D = int(s[a+b+c:a+b+c+d])
                            if A<256 and B<256 and C<256 and D<256:
                                ip = [str(A),str(B),str(C),str(D)]
                                ip = '.'.join(ip)
                                if len(ip)==s_len+3: ## 很关键一部，出去了‘001’这种情况
                                    ip_list.append(ip)
        return ip_list




if __name__ == '__main__':
    s = "255.255.255.2"
    # ip_list = Solution().restoreIpAddresses(s)
    # for ip in ip_list:
    #     print(ip)
    ip_list = Solution1().restoreIpAddresses(s)
    for ip in ip_list:
        print(ip)
