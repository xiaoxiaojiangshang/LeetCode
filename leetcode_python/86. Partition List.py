#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2018/11/18 19:37   
#  IDE：PyCharm 
import numpy as np

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        l1 = h1 = ListNode(-1) #小于x
        l2 = h2 = ListNode(-1) #大于x
        while head != None:
            if head.val <x:
                l1.next = head
                l1 = l1.next
                # l1.next = None
            else:
                l2.next = head
                l2 = l2.next
                # l2.next = None
            head = head.next
        l1.next = h2.next
        l2.next = None
        return h1.next



if __name__ == '__main__':
    list_nodes = [1,4,3,2,5,2]
    l1 = head = ListNode(-1)
    for i_node in list_nodes:
        l2 = ListNode(i_node)
        l1.next = l2
        l1 = l1.next
    head = Solution().partition(head.next,3)
    while head != None:
        print(head.val)
        head = head.next

