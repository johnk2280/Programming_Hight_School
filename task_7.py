class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        egg = self.compare(value, self.head.value)
        if egg <= 0 and self.__ascending or egg >= 0 and not self.__ascending:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        egg = self.compare(value, self.tail.value)
        if egg >= 0 and self.__ascending or egg <= 0 and not self.__ascending:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return

        node = self.head.next
        while node:
            egg = self.compare(value, node.value)
            if egg <= 0 and self.__ascending or egg >= 0 and not self.__ascending:
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
                break
            node = node.next

    def find(self, val):
        node = self.head
        while node:
            egg = self.compare(val, node.value)
            if egg == 0:
                return node
            if egg < 0 and self.__ascending or egg > 0 and not self.__ascending:
                break
            node = node.next
        return

    def delete(self, val):
        if not self.head:
            return
        egg_head = self.compare(val, self.head.value)
        egg_tail = self.compare(val, self.tail.value)
        if egg_head < 0 and self.__ascending or egg_head > 0 and not self.__ascending:
            return
        if egg_tail > 0 and self.__ascending or egg_tail < 0 and not self.__ascending:
            return
        if egg_head == 0 and self.head.next:
            self.head = self.head.next
            self.head.prev = None
        elif egg_head == 0 and self.head.next is None:
            self.head = None
            self.tail = None
            return
        if egg_tail == 0:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        node = self.head.next
        while node:
            egg = self.compare(val, node.value)
            if egg == 0:
                node.prev.next = node.next
                node.next.prev = node.prev
                break
            if egg < 0 and self.__ascending or egg > 0 and not self.__ascending:
                break
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        l_v1 = len(v1.strip())
        l_v2 = len(v2.strip())
        if l_v1 < l_v2:
            return -1
        if l_v1 > l_v2:
            return 1
        return 0
