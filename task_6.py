class Deque:
    def __init__(self):
        self.deque = LinkedList2()

    def addFront(self, item):
        node = Node(item)
        if self.deque.head is None:
            self.deque.tail = node
            node.next = None
            node.prev = None
        else:
            node.next = self.deque.head
            self.deque.head.prev = node
        self.deque.head = node

    def addTail(self, item):
        node = Node(item)
        if self.deque.head is None:
            self.deque.head = node
        else:
            self.deque.tail.next = node
            node.prev = self.deque.tail
        self.deque.tail = node

    def removeFront(self):
        if self.deque.head:
            remove_val = self.deque.head.value
            self.deque.head = self.deque.head.next
            return remove_val
        return None

    def removeTail(self):
        if self.deque.tail is None:
            return

        remove_val = self.deque.tail.value
        if self.deque.tail == self.deque.head:
            self.deque.tail = None
            self.deque.head = None
            return remove_val

        self.deque.tail = self.deque.tail.prev
        self.deque.tail.next = None
        return remove_val

    def size(self):
        node = self.deque.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

