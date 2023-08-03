"""
LRU
"""


class LinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity: int):
        self.map = dict()  # 创建hash map
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.removeHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            node = self.map[key]
            node.value = value
            self.removeHead(node)
        else:
            if self.capacity == len(self.map):
                self.map.pop(self.deleteTail())

            node = LinkNode(key, value)
            self.map[key] = node
            self.makehead(node)

    def removeHead(self, node):
        self.deleteNode(node)
        self.makehead(node)

    def deleteTail(self):
        node = self.tail.prev
        self.deleteNode(node)
        return node.key

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def makehead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
