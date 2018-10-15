class CacheNode():

    def __init__(self, key, value, prev = None, next = None):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value

class LRUCache():
    def __init__(self, size, nodes = dict(), first = None, last = None):
        self.size = size
        self.nodes = nodes
        self.first = first
        self.last = last

    def getNode(self, key):
        if self.nodes is None or len(self.nodes) == 0:
            return None
        node = self.nodes.get(key)
        if node:
            self.move2head(node)
        self.showNodes()
        return node

    def putNode(self, key, value):
        if self.nodes is None:
            return
        node = self.nodes.get(key)
        currentSize = len(self.nodes)
        if node is None:
            if currentSize >= self.size:
                self.popLastNode()
            node = CacheNode(key, value)
        self.move2head(node)
        self.nodes[key] = node

        self.showNodes()

    def move2head(self, node):
        if self.first is not None and node.key == self.first.key:
            return
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if self.last is not None and node.key == self.last.key:
            last = node.prev
        if self.first is not None:
            node.next = self.first
            self.first.prev = node

        self.first = node
        node.prev = None
        if self.last is None:
            self.last = self.first


    def popLastNode(self):
        if self.last is not None:
            if self.last.prev is not None:
                self.last.prev.next = None
            else:
                self.first = None

            self.nodes.pop(self.last.key)

            self.last = self.last.prev

    def showNodes(self):
        for key, value in self.nodes.iteritems():
            node = self.nodes.get(key)
            print('current:', node.key, node.value)


def main():
    cache = LRUCache(4)
    print('put a')
    cache.putNode('a', 'hehe')
    print('put b')
    cache.putNode('b', 'hehe')
    print('put c')
    cache.putNode('c', 'hehe')
    print('put d')
    cache.putNode('d', 'hehe')
    print('get b')
    cache.getNode('b')
    print('put e')
    cache.putNode('e', 'hehe')
    print('put a')
    cache.putNode('a', 'hehe')
main()
