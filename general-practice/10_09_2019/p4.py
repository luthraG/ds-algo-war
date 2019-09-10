class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        # Create dummy head and tail
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

        if node != self.tail:
            self.head.next = node.next
            node.next.prev = self.head

            node.next = None
            node.prev = None
            node = None
        else:
            print('List is empty. Nothing to delete')

    def remove_from_end(self):
        node = self.tail.prev

        if node != self.head:
            self.tail.prev = node.prev
            node.prev.next = self.tail
        else:
            print('List is empty. Nothing to delete')
    
    def traverse_from_start(self):
        node = self.head.next

        while node != self.tail:
            print(node.data)
            node = node.next

    def traverse_from_end(self):
        node = self.tail.prev

        while node != self.head:
            print(node.data)
            node = node.prev

    def count(self):
        node = self.head.next
        c = 0

        while node != self.tail:
            c += 1
            node = node.next
        return c

if __name__ == '__main__':
    doubleLinkedList = DoubleLinkedList()
    number = int(input('Enter the number of items to be added to list :: '))
    for i in range(number):
        data = int(input('Enter the data :: '))
        if i & 1 == 1:
            doubleLinkedList.add_to_end(data)
        else:
            doubleLinkedList.add_to_start(data)
    
    count = doubleLinkedList.count()
    print('Total items in list :: {}'.format(count))
    print('Items from start are')
    doubleLinkedList.traverse_from_start()

    MAX_ALLOWED = 2
    diff = count - MAX_ALLOWED
    if diff > 0:
        print('Going to delete {} items from start'.format(diff))
        for i in range(diff):
            doubleLinkedList.remove_from_start()
    
    print('Total items in list are :: {}'.format(doubleLinkedList.count()))
    print('Items in list from end are')
    doubleLinkedList.traverse_from_end()