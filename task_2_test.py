import unittest
from task_2 import *


class FindOnce(unittest.TestCase):

    def test_find_func_returns_node(self):
        a_list = LinkedList2()
        b_list = LinkedList2()

        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(1)
        n4 = Node(4)
        n5 = Node(1)
        n6 = Node(6)

        self.assertEqual(a_list.find(1), None)

        a_list.add_in_tail(n1)
        self.assertEqual(a_list.find(1), n1)

        a_list.add_in_tail(n2)
        a_list.add_in_tail(n3)
        a_list.add_in_tail(n4)
        a_list.add_in_tail(n5)
        self.assertEqual(a_list.find(1), n1)
        self.assertEqual(a_list.find(4), n4)
        self.assertEqual(a_list.find(2), n2)

        a_list.add_in_tail(n6)
        self.assertEqual(a_list.find(6), n6)

        b_list.add_in_tail(n2)
        b_list.add_in_tail(n1)
        b_list.add_in_tail(n3)
        self.assertEqual(a_list.find(1), n1)


class FindEmAll(unittest.TestCase):

    def test_find_all_func_returns_list(self):
        a_list = LinkedList2()

        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(1)
        n4 = Node(4)
        n5 = Node(1)
        n6 = Node(6)

        self.assertEqual(a_list.find_all(1), [])

        a_list.add_in_tail(n1)
        self.assertEqual(a_list.find_all(1), [n1])

        a_list.add_in_tail(n2)
        a_list.add_in_tail(n3)
        self.assertEqual(a_list.find_all(1), [n1, n3])

        a_list.add_in_tail(n4)
        a_list.add_in_tail(n5)
        a_list.add_in_tail(n6)
        self.assertEqual(a_list.find_all(1), [n1, n3, n5])
        self.assertEqual(a_list.find_all(2), [n2])
        self.assertEqual(a_list.find_all(4), [n4])
        self.assertEqual(a_list.find_all(6), [n6])


class DeleteEmAll(unittest.TestCase):

    def test_delete_func_empty_list(self):
        a_list = LinkedList2()

        a_list.delete(1)
        self.assertEqual(a_list.__dict__, {'head': None, 'tail': None})

        a_list.delete(1, True)
        self.assertEqual(a_list.__dict__, {'head': None, 'tail': None})
        self.assertEqual(a_list.len(), 0)

    def test_delete_func_one_node_list(self):
        b_list = LinkedList2()
        n1 = Node(5)

        b_list.add_in_tail(n1)
        self.assertEqual(b_list.len(), 1)

        b_list.delete(5)
        self.assertEqual(b_list.__dict__, {'head': None, 'tail': None})

        b_list.add_in_tail(n1)
        b_list.delete(5, True)
        self.assertEqual(b_list.__dict__, {'head': None, 'tail': None})
        self.assertEqual(b_list.len(), 0)

    def test_delete_func_two_equal_nodes_list(self):
        c_list = LinkedList2()
        n1 = Node(2)
        n2 = Node(2)
        n3 = Node(2)

        c_list.add_in_tail(n1)
        c_list.add_in_tail(n2)
        self.assertEqual(c_list.len(), 2)

        c_list.delete(2)
        self.assertEqual(c_list.__dict__, {'head': n2, 'tail': n2})
        self.assertEqual(c_list.len(), 1)

        c_list.add_in_tail(n3)
        self.assertEqual(c_list.__dict__, {'head': n2, 'tail': n3})

        c_list.delete(2, True)
        self.assertEqual(c_list.__dict__, {'head': None, 'tail': None})

    def test_delete_func_two_not_equal_nodes_list(self):
        c_list = LinkedList2()
        # d_list = LinkedList2()
        d_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        c_list.add_in_tail(n1)
        c_list.add_in_tail(n2)
        d_list.add_in_head(n3)
        d_list.add_in_head(n4)

        c_list.delete(1)
        self.assertEqual(c_list.__dict__, {'head': n2, 'tail': n2})
        self.assertEqual(c_list.head.next, None)
        self.assertEqual(c_list.tail.next, None)

        d_list.delete(3)
        self.assertEqual(d_list.__dict__, {'head': n4, 'tail': n4})
        self.assertEqual(d_list.head.next, None)
        self.assertEqual(d_list.tail.next, None)

        d_list.add_in_tail(n5)
        d_list.add_in_tail(n6)
        d_list.delete(6)
        self.assertEqual(d_list.__dict__, {'head': n4, 'tail': n5})
        self.assertEqual(d_list.head.next, d_list.tail)
        self.assertEqual(d_list.tail.next, None)


    def test_delete_func_three_equal_nodes_ih_head_list(self):
        d_list = LinkedList2()
        n1 = Node(2)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(3)
        n5 = Node(4)
        n6 = Node(5)
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        d_list.add_in_tail(n6)

        d_list.delete(2, True)
        self.assertEqual(d_list.__dict__, {'head': n4, 'tail': n6})
        self.assertEqual([d_list.head, d_list.head.next, d_list.head.next.next],
                         [d_list.tail.prev.prev, d_list.tail.prev, d_list.tail])

    def test_delete_func_three_equal_nodes_ih_tail_list(self):
        e_list = LinkedList2()
        n1 = Node(2)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(3)
        n5 = Node(4)
        n6 = Node(5)
        e_list.add_in_tail(n6)
        e_list.add_in_tail(n5)
        e_list.add_in_tail(n4)
        e_list.add_in_tail(n1)
        e_list.add_in_tail(n2)
        e_list.add_in_tail(n3)

        e_list.delete(2, True)
        self.assertEqual(e_list.__dict__, {'head': n6, 'tail': n4})
        self.assertEqual([e_list.head, e_list.head.next, e_list.head.next.next],
                         [e_list.tail.prev.prev, e_list.tail.prev, e_list.tail])

    def test_delete_func_several_equal_nodes_list(self):
        f_list = LinkedList2()
        n1 = Node(2)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(3)
        n5 = Node(4)
        n6 = Node(5)
        f_list.add_in_tail(n1)
        f_list.add_in_tail(n5)
        f_list.add_in_tail(n4)
        f_list.add_in_tail(n2)
        f_list.add_in_tail(n6)
        f_list.add_in_tail(n3)

        f_list.delete(2)
        self.assertEqual(f_list.__dict__, {'head': n5, 'tail': n3})

        f_list.delete(2, True)
        self.assertEqual(f_list.__dict__, {'head': n5, 'tail': n6})
        self.assertEqual([f_list.head, f_list.head.next, f_list.head.next.next],
                         [n5, n4, n6])


class InsertIt(unittest.TestCase):

    def test_insert_empty_list(self):
        a_list = LinkedList2()
        n1 = Node('5')

        a_list.insert(None, n1)
        self.assertEqual(a_list.__dict__, {'head': n1, 'tail': n1})
        self.assertEqual(a_list.len(), 1)

    def test_insert_not_empty_list(self):
        b_list = LinkedList2()
        n1 = Node('1')
        n2 = Node('2')
        b_list.add_in_head(n1)

        b_list.insert(None, n2)
        self.assertEqual(b_list.__dict__, {'head': n1, 'tail': n2})
        self.assertEqual(b_list.len(), 2)

    def test_insert_not_empty_list_middle_insert(self):
        c_list= LinkedList2()
        n1 = Node('1')
        n2 = Node('2')
        n3 = Node('qwerty')
        c_list.add_in_tail(n1)
        c_list.add_in_head(n2)

        c_list.insert(n2, n3)
        self.assertEqual(c_list.__dict__, {'head': n2, 'tail': n1})
        self.assertEqual(c_list.len(), 3)
        self.assertEqual([c_list.head, c_list.head.next, c_list.head.next.next],
                         [n2, n3, n1])

    def test_insert_not_empty_list_tail_insert(self):
        d_list = LinkedList2()
        n1 = Node('117')
        n2 = Node(0.25)
        n3 = Node('qwerty')
        n4 = Node(None)
        n5 = Node(1)
        n6 = Node(1)
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n4)
        d_list.add_in_head(n2)

        d_list.insert(n4, n3)
        self.assertEqual(d_list.len(), 4)
        self.assertEqual(d_list.__dict__, {'head': n2, 'tail': n3})
        self.assertEqual([d_list.head, d_list.head.next, d_list.head.next.next, d_list.head.next.next.next],
                         [n2, n1, n4, n3])

        d_list.insert(n6, n5)
        self.assertEqual(d_list.__dict__, {'head': n2, 'tail': n3})
        self.assertEqual([d_list.head, d_list.head.next, d_list.head.next.next, d_list.head.next.next.next],
                         [n2, n1, n4, n3])


class AddInHead(unittest.TestCase):

    def test_add_in_head_func_empty_list(self):
        a_list = LinkedList2()
        n1 = Node(1)
        a_list.add_in_head(n1)
        self.assertEqual(a_list.__dict__, {'head': n1, 'tail': n1})

    def test_add_in_head_func_one_node_list(self):
        b_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(1)
        b_list.add_in_tail(n1)
        b_list.add_in_head(n2)
        self.assertEqual(b_list.__dict__, {'head': n2, 'tail': n1})

    def test_add_in_head_func_multiple_nodes_list(self):
        c_list = LinkedList2()
        n1 = Node(10)
        n2 = Node(11)
        n3 = Node(12)
        n4 = Node(117)
        c_list.add_in_tail(n1)
        c_list.add_in_tail(n2)
        c_list.add_in_tail(n3)
        c_list.add_in_head(n4)
        self.assertEqual(c_list.__dict__, {'head': n4, 'tail': n3})
        self.assertEqual(c_list.len(), 4)
        self.assertEqual([c_list.head, c_list.head.next, c_list.head.next.next, c_list.head.next.next.next],
                         [c_list.tail.prev.prev.prev, c_list.tail.prev.prev, c_list.tail.prev, c_list.tail])
        self.assertEqual(c_list.head.prev, None)
        self.assertEqual(c_list.tail.next, None)





