class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = Node("||HEAD||")
        self.tail = Node("||TAIL||")

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_start(self, item):
        node = Node(item)
        temp = self.head.next

        node.next = temp
        node.prev = self.head

        self.head.next = node

        temp.prev = node

    def add_to_end(self, item):
        node = Node(item)
        temp = self.tail.prev

        node.next = self.tail
        node.prev = temp

        temp.next = node

        self.tail.prev = node

    def remove_at_start(self):
        node = self.head.next
        # Handle base case
        if node.next is None:
            print('List is empty')
        else:
            self.head.next = node.next
            node.next.prev = self.head

            node.next = None
            node.prev = None
            node = None
    
    def remove_from_last(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        node.next = None
        node.prev = None
        node = None

    def count(self):
        c = 0
        node = self.head.next
        while node.next is not None:
            c += 1
            node = node.next

        return c

    def traverse_from_start(self):
        node = self.head.next
        if node.next is None:
            print('List is empty')
            return

        while node.next is not None:
            print(node.item)
            node = node.next

    def traverse_from_last(self):
        node = self.tail.prev

        if node.prev is None:
            print('List is empty')
        else:
            while node.prev is not None:
                print(node.item)
                node = node.prev

if __name__ == '__main__':
    doubleLinkedList = DoubleLinkedList()
    doubleLinkedList.add_to_end(7)
    doubleLinkedList.add_to_end(9)
    doubleLinkedList.add_to_start(5)
    print('Total items count :: {}'.format(doubleLinkedList.count()))
    print('Items from start')
    doubleLinkedList.traverse_from_start()
    print('Items from last')
    doubleLinkedList.traverse_from_last()
