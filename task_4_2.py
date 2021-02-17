# Переделайте реализацию стека так,
# чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой.


class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        count = 0
        node = self.stack.tail
        while node is not None:
            count += 1
            node = node.prev

        return count

    def pop(self):
        if self.stack.head is None:
            return

        pop_value = self.stack.head.value
        if self.stack.tail == self.stack.head:
            self.stack.tail = None
            self.stack.head = None
            return pop_value

        self.stack.head = self.stack.head.next
        self.stack.head.prev = None
        return pop_value

    def push(self, value):
        node = Node(value)
        if self.stack.tail is None:
            self.stack.tail = node
            self.stack.tail.prev = None
            self.stack.tail.next = None
        else:
            node.next = self.stack.head
            self.stack.head.prev = node
        self.stack.head = node

    def peek(self):
        if self.stack.head is not None:
            return self.stack.head.value

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

