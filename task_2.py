class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        if self.head is None:
            return

        node = self.head
        while node is not None:
            if node.value != val:
                node = node.next
            elif node.value == val and node.prev is None and node.next is None:
                self.head = None
                node = None
            elif node.value == val and node.prev is None and node.next is not None:
                self.head = node.next
                self.head.prev = None
                if all is False:
                    break
                node = self.head
            elif node.value == val and node.prev is not None and node.next is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
                node = node.prev
                if all is False:
                    break
            elif node.value == val and node.prev is not None and node.next is None:
                self.tail = node.prev
                node.prev.next = None
                node = None

        if self.head is None:
            self.tail = None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                newNode.next = None
                newNode.prev = None
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
            self.tail = newNode
            return

        node = self.head
        while node is not None:
            if node == afterNode:
                if node != self.tail:
                    newNode.next = node.next
                    node.next.prev = newNode

                node.next = newNode
                newNode.prev = node

                if node == self.tail:
                    self.tail = newNode
                    return
                return
            node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
