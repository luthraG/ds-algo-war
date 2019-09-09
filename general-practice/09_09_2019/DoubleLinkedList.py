class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        # Create dummy head and dummy tails
        self.head = Node()
        self.tail = Node()

        # Associate head and tails
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # add a nodes at start of list
    def add_to_start(self, data):
        node = Node(data)

        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

    # adds a node to last of list
    def add_to_last(self, data):
        node = Node(data)

        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    # remove a node from begining
    def remove_from_start(self):
        # Handle base case when list is empty
        if self.head.next == self.tail:
            print('List is empty. Nothing to delete')
        else:
            node = self.head.next

            self.head.next = node.next
            node.next.prev = self.head

            node.next = None
            node.prev = None
            node = None

    # remove a node from last position
    def remove_from_last(self):
        # handle base case
        if self.tail.prev == self.head:
            print('List is empty. Nothing to delete')
        else:
            node = self.tail.prev

            self.tail.prev = node.prev
            node.prev.next = self.tail

            node.prev = None
            node.next = None
            node = None

    # Traverse a list from start
    def traverse_from_start(self):
        # handle base case
        if self.head.next == self.tail:
            print('List is empty')
        else:
            node = self.head.next
            while node.data is not None:
                print(node.data)
                node = node.next

    # Traverse a list from end
    def traverse_from_last(self):
        # Handle base case
        if self.tail.prev == self.head:
            print('Lits is empty')
        else:
            node = self.tail.prev
            while node.data is not None:
                print(node.data)
                node = node.prev
    
    # count list items
    def count(self):
        c = 0
        node = self.head.next
        while node.data is not None:
            c += 1
            node = node.next
        return c

if __name__ == '__main__':
    doubleLinkedList = DoubleLinkedList()

    number_start = int(input('Enter number of nodes to add at start :: '))
    number_end = int(input('Enter number of nodes to add at last :: '))

    for i in range(number_start):
        data = int(input('Enter data for node to be added at start :: '))
        doubleLinkedList.add_to_start(data)
    
    print('Data in list... Traversing from start...')
    doubleLinkedList.traverse_from_start()
    print('========================================')
    print('Data in list... Traversing from last....')
    doubleLinkedList.traverse_from_last()
    print('========================================')

    for i in range(number_end):
        data = int(input('Enter data for node to be added at end :: '))
        doubleLinkedList.add_to_last(data)
    
    print('Data in list... Traversing from start...')
    doubleLinkedList.traverse_from_start()
    print('========================================')
    print('Data in list... Traversing from last....')
    doubleLinkedList.traverse_from_last()
    print('========================================')

    print('Total nodes in the list : {}'.format(doubleLinkedList.count()))

    print('========================================')
    print('Removing 1 node from begining')
    doubleLinkedList.remove_from_start()
    print('Removing 1 node from end')
    doubleLinkedList.remove_from_last()
    print('Data in list... Traversing from start...')
    doubleLinkedList.traverse_from_start()
    print('========================================')