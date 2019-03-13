#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/23 20:36   
#  IDE：PyCharm 
import numpy as np
import copy

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n : return head
        count = 1
        pre, curr, next, revers = ListNode(-1), head, ListNode(-1), None
        pre.next = head
        while count<m:
            pre = curr
            curr = curr.next
            count +=1
        while count <n+1: # 非常考验链表操作
            next = curr.next
            curr.next = revers
            revers = curr
            curr = next
            count +=1
        if m==1: head = revers # 为了防止m等于丢失情况。
        if pre.next != None:
            pre.next.next = curr
            pre.next = revers
        return head


if __name__ == '__main__':
    list_nodes = [1,2,3,4,5,6,7]
    l1 = head = ListNode(-1)
    for i_node in list_nodes:
        l2 = ListNode(i_node)
        l1.next = l2
        l1 = l1.next
    head = Solution().reverseBetween(head.next,1,1)
    while head != None:
        print(head.val)
        head = head.next