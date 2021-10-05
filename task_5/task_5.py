class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        node = Node(item)
        if self.queue.head is None:
            self.queue.head = node
        else:
            self.queue.tail.next = node
        self.queue.tail = node

    def dequeue(self):
        if self.queue.head:
            deq_val = self.queue.head.value
            self.queue.head = self.queue.head.next
            return deq_val
        return None

    def size(self):
        node = self.queue.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
