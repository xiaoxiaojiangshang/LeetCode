# -*- ecoding: utf-8 -*-
# @ModuleName: LFU_Cache_460
# @Function: leetcode
# @Author: 姜贵平
# @Time: 2021/7/4 23:02


## 节点
class DoubleLinkNode(object):
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = None

## 双向列表
class DoubleLinkList(object):
    
    ## 初始话创建列表
    def __init__(self):
        self.head = DoubleLinkNode(0,0)
        self.tail = DoubleLinkNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    ## 包含两个操作，add and remove
    def remove(self,node:DoubleLinkNode):
        node.next.prev = node.prev
        node.prev.next = node.next
        del node
    
    ## 加入头部
    def add(self,node:DoubleLinkNode):
        # 后
        self.head.next.prev = node
        node.next = self.head.next
        ## 前
        self.head.next = node
        node.prev = self.head

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 1
        ## 记录频次
        self.freq2nodeList = {}
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        freq, value = node.freq, node.value
        ## 先删除原来的freq 里面的节点
        node_list = self.freq2nodeList[freq]
        node_list.remove(node)
        if self.minFreq == freq and node_list.head.next == node_list.tail: ## 为空注意判断
            self.minFreq += 1
        nowFreq = freq + 1
        if nowFreq not in self.freq2nodeList:
            nodeList = DoubleLinkList()
            self.freq2nodeList[nowFreq] = nodeList
        else:
            nodeList = self.freq2nodeList[nowFreq]
        nodeList.add(node)
        node.freq = nowFreq ## 更新一下频率
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        ## 存在 或者不存在
        if key in self.dict:
            self.get(key)
            self.dict[key].value = value ## 注意更新value
        else:
            if len(self.dict) == self.capacity:
                ## 要删除的list
                nodeList = self.freq2nodeList[self.minFreq]
                node = nodeList.tail.prev
                nodeList.remove(node)
                del self.dict[node.key]
            newNode = DoubleLinkNode(key, value)
            newNode.freq = 1
            self.minFreq = 1
            if self.minFreq not in self.freq2nodeList:
                nodeList = DoubleLinkList()
                self.freq2nodeList[self.minFreq] = nodeList
            else:
                nodeList = self.freq2nodeList[self.minFreq]
            nodeList.add(newNode)
            self.dict[key] = newNode

if __name__ == '__main__':
    capacity = 10
    lfu = LFUCache(capacity)
    op_list = ["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    data = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
    for index,op in enumerate(op_list):
        if op == 'put':
            key,value = data[index]
            lfu.put(key,value)
            print('null')
        elif op == 'get':
            if index == 94:
                a = 1
            print(lfu.get(data[index][0]))

    