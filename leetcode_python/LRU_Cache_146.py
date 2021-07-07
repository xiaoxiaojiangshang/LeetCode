
class Double_Link_Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Double_Link_Node(0,0)
        self.tail = Double_Link_Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    ## 删除节点
    def remove_node(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        del node
    ## 添加节点
    def add_node(self,node):
        ## 后
        self.head.next.prev = node
        node.next = self.head.next
        ## 前
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        try:
            ## 获取节点
            node = self.dict[key]
            self.remove_node(node)
            self.add_node(node)
            return node.value
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        ## 应该分两种情况，在字典里面，和不在
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.remove_node(node)
            self.add_node(node)
        else:
            ## 分两种
            new_node = Double_Link_Node(key,value)
            if len(self.dict) == self.capacity:
                last_node = self.tail.prev
                del self.dict[last_node.key]
                self.remove_node(last_node)
            self.dict[key] = new_node
            self.add_node(new_node)

if __name__ == '__main__':
    capacity = 2
    lRUCache = LRUCache(capacity)
    lRUCache.put(2, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(2))
    lRUCache.put(1, 1)
    lRUCache.put(4, 1)
    print(lRUCache.get(2))
