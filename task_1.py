class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        node = self.head
        prev_node = None

        while node is not None:
            if node.value != val:
                prev_node = node
                node = node.next
            elif node.value == val and node == self.head:
                self.head = node.next
                node = self.head
                if all is False:
                    break
            elif node.value == val and node != self.tail:
                prev_node.next = node.next
                node = prev_node
                if all is False:
                    break
            self.tail = prev_node

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
            new_head = Node(newNode)
            if self.head is None:
                self.head = new_head
                self.tail = new_head
                return
            new_head.next = self.head
            self.head = new_head
            return

        node = self.head

        while node is not None:
            if node.value == afterNode:
                new_node = Node(newNode)
                new_node.next = node.next
                node.next = new_node
                if node == self.tail:
                    self.tail = new_node
                    return
                return
            node = node.next
