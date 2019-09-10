class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, max_entries = 5):
        self.max_entries_count = max_entries
        self.current_entries_count = 0

        # Create dummy head and tail
        self.head = Node()
        self.tail = Node()

        # Associate head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

        # hash map/table for fetching items in constant time
        self.hash_map = {}

    # Given a key, it fetches the value if present
    # returns -1 if no key/value is present
    def get(self, key):
        if key in self.hash_map:
            node = self.hash_map[key]

            # Move node to bring it a front
            # It keeps most recently used item at front
            self.moveNode(node)

            # return value to client
            return node.value
        else:
            return -1

    def moveNode(self, node):
        # remove node from its position and add it at front
        self.removeNode(node)
        self.addNode(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    # Given key/value it either adds data in cache, if it does not exists
    # or it updates the data in cache, if it exists
    def set(self, key, value):
        if key in self.hash_map:
            # key exists
            # update value
            # update entry in hash_map
            # move node to front
            node = self.hash_map[key]
            node.value = value
            self.hash_map[key] = node
            self.moveNode(node)
        else:
            # does not exists
            # create node
            # add to hash_map
            # increase the counter for current entries
            # add node to front
            # check if it exceeds the count for max entries
            node = Node(key, value)

            self.hash_map[key] = node
            self.current_entries_count += 1

            self.addNode(node)

            if self.current_entries_count > self.max_entries_count:
                self.removeLastNode()
                # reduce the current entries count
                self.current_entries_count -= 1

    def removeLastNode(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev

        node.next = None
        node.prev = None

        # remove from hash_map
        del self.hash_map[node.key]

    def count(self):
        node = self.head.next
        c = 0

        while node != self.tail:
            c += 1
            node = node.next
        
        return c

    def keys(self):
        node = self.head.next
        key = []

        while node != self.tail:
            key.append(node.key)
            node = node.next
        
        return key

if __name__ == '__main__':
    cache = LRUCache(3)
    print('Total items in cache :: {}'.format(cache.count()))
    cache.set('name', 'Gaurav Luthra')
    cache.set('age', 30)
    cache.set('sex', 'M')
    print('Total items in cache :: {}'.format(cache.count()))
    print('Keys in cache are : {}'.format(cache.keys()))
    cache.set('spouse', 'Bhawna')
    print('Total items in cache :: {}'.format(cache.count()))
    print('Keys in cache are : {}'.format(cache.keys()))