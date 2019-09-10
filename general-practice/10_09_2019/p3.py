class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = Node()
    
    def add_to_start(self, data):
        node = Node(data)
        node.next = self.start_node.next
        self.start_node.next = node
    
    def add_to_end(self, data):
        node = Node(data)
        n = self.start_node

        while n.next is not None:
            n = n.next
        
        n.next = node

    def remove_from_begining(self):
        node = self.start_node.next
        if node is None:
            print('List is empty. Nothing to delete')
        else:
            self.start_node.next = node.next
            node = None
    
    def remove_from_end(self):
        node = self.start_node
        if node.next is None:
            print('List is empty. Nothing to delete')
        else:
            while node.next.next is not None:
                node = node.next
            
            node.next = None
    
    def traverse_list(self):
        node = self.start_node
        while node is not None:
            if node.data is not None:
                print(node.data)
            node = node.next
    
    def count(self):
        c = 0
        node = self.start_node
        while node is not None:
            if node.data is not None:
                c += 1
            node = node.next

        return c

if __name__ == '__main__':
    linkedList = LinkedList()
    number = int(input('Enter number of items to add in list :: '))
    for i in range(number):
        data = int(input('Enter data :: '))
        # If i is even then add to start, else add to end
        if i & 1 == 1:
            linkedList.add_to_end(data)
        else:
            linkedList.add_to_start(data)
    count = linkedList.count()
    print('Total items in the list :: {}'.format(count))

    MAX_ALLOWED = 2
    diff = count - MAX_ALLOWED
    if diff > 0:
        print('Going to remove {} items from end'.format(diff))
        for i in range(diff):
            linkedList.remove_from_end()
    
    print('List items are')
    linkedList.traverse_list()
    print('Total items in the list :: {}'.format(linkedList.count()))

