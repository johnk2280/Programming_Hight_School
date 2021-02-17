class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        count = 0
        node = self.stack.head
        while node is not None:
            count += 1
            node = node.next

        return count

    def pop(self):  # Доработать
        if self.stack.tail is None:
            return

        pop_value = self.stack.tail.value
        if self.stack.tail == self.stack.head:
            self.stack.tail = None
            self.stack.head = None
            return pop_value

        self.stack.tail = self.stack.tail.prev
        self.stack.tail.next = None
        return pop_value

    def push(self, value):
        node = Node(value)
        if self.stack.head is None:
            self.stack.head = node
            self.stack.head.prev = None
            self.stack.head.next = None
        else:
            self.stack.tail.next = node
            node.prev = self.stack.tail
        self.stack.tail = node

    def peek(self):
        if self.stack.tail is not None:
            return self.stack.tail.value

        return None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

