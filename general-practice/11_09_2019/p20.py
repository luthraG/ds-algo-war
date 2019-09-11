class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
    def __init__(self):
        # Create dummy head and tails
        self.head = Node()
        self.tail = Node()

        # Associate head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_start(self, data):
        node = Node(data)
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node
    
    def add_to_end(self, data):
        node = Node(data)
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def remove_from_start(self):
        node = self.head.next
        if node == self.tail:
            print('List is empty. Nothing to delete')
        else:
            self.head.next = node.next
            node.next.prev = self.head

            node.next = None
            node.prev = None
            node = None

    def remove_from_end(self):
        node = self.tail.prev
        if node == self.head:
            print('List is empty. Nothing to delete')
        else:
            self.tail.prev = node.prev
            node.prev.next = self.tail

            node.next = None
            node.prev = None
            node = None
    
    def count(self):
        c = 0
        node = self.head.next
        while node != self.tail:
            c += 1
            node = node.next

        return c
    
    def traverse_from_start(self):
        node = self.head
        while node != self.tail:
            if node.data is not None:
                print(node.data)
            node = node.next

    def traverse_from_end(self):
        node = self.tail
        while node != self.head:
            if node.data is not None:
                print(node.data)
            node = node.prev

if __name__ == '__main__':
    linkedList = DoubleLinkedList()
    number = int(input('Enter the number of nodes to be added :: '))
    for i in range(number):
        if i & 1 == 1:
            linkedList.add_to_start(int(input('Enter data :: ')))
        else:
            linkedList.add_to_end(int(input('Enter data :: ')))
    
    count = linkedList.count()
    print('Total items in list are :: {}'.format(count))

    print('Items in list from start to end are')
    linkedList.traverse_from_start()

    print('Items in list from end to start are')
    linkedList.traverse_from_end()

    print('Going to delete {} items from list from end'.format(count // 2))
    for i in range(count // 2):
        linkedList.remove_from_end()
    
    count = linkedList.count()
    print('Total items in list are :: {}'.format(count))

    print('Items in list from start to end are')
    linkedList.traverse_from_start()

    print('Items in list from end to start are')
    linkedList.traverse_from_end()