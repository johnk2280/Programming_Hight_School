import unittest
from task_1 import *
import random


class FindEmAll(unittest.TestCase):

    def test_find_all_func_returns_list(self):
        a_list = LinkedList()
        b_list = LinkedList()
        c_list = LinkedList()

        temp_list1 = [1, 2, 3, 4, 5, 5, 5]

        for i in temp_list1:
            a_list.add_in_tail(Node(i))

        c_list.add_in_tail(Node(1))

        self.assertEqual(a_list.find_all(1), [a_list.head])
        self.assertEqual(a_list.find_all(5), [a_list.head.next.next.next.next,
                                              a_list.head.next.next.next.next.next,
                                              a_list.head.next.next.next.next.next.next])
        self.assertEqual(a_list.find_all(2), [a_list.head.next])
        self.assertEqual(a_list.find_all(3), [a_list.head.next.next])
        self.assertEqual(a_list.find_all(4), [a_list.head.next.next.next])
        self.assertEqual(b_list.find_all(0), [])
        self.assertEqual(c_list.find_all(1), [c_list.head])
        self.assertEqual(c_list.find_all(1), [c_list.tail])


class DeleteEmAll(unittest.TestCase):

    def test_delete_func_returns_dict(self):
        a_list = LinkedList()
        b_list = LinkedList()
        c_list = LinkedList()
        d_list = LinkedList()

        temp_list1 = [1, 1]
        temp_list2 = [1, 2, 3, 4, 5, 5, 5]

        a_list.add_in_tail(Node(1))

        for i in temp_list1:
            b_list.add_in_tail(Node(i))
        for j in temp_list2:
            c_list.add_in_tail(Node(j))

        a_list.delete(1)
        self.assertEqual({'head': None, 'tail': None}, a_list.__dict__)

        b_list.delete(1, True)
        self.assertEqual({'head': None, 'tail': None}, b_list.__dict__)

        c_list.delete(5, True)
        self.assertEqual({'head': c_list.head, 'tail': c_list.head.next.next.next}, c_list.__dict__)

        d_list.delete(1)
        self.assertEqual({'head': None, 'tail': None}, d_list.__dict__)


class CleanItUp(unittest.TestCase):

    def test_clean_func_returns_dict(self):
        a_list = LinkedList()
        c_list = LinkedList()

        temp_list1 = [1, 2, 3, 4, 5, 5, 5]

        for i in temp_list1:
            a_list.add_in_tail(Node(i))

        a_list.clean()
        self.assertEqual(c_list.__dict__, a_list.__dict__)

        a_list.add_in_tail(Node(1))
        a_list.clean()
        self.assertEqual(c_list.__dict__, a_list.__dict__)


class CountEmAll(unittest.TestCase):

    def test_len_func_returns_integer(self):
        a_list = LinkedList()
        b_list = LinkedList()
        c_list = LinkedList()
        d_list = LinkedList()

        temp_list1 = [i for i in range(100)]
        temp_list2 = [chr(random.randint(40, 128)) for _ in range(100)]

        for i in temp_list1:
            a_list.add_in_tail(Node(i))

        b_list.add_in_tail(Node(10))

        for j in temp_list2:
            c_list.add_in_tail(Node(j))

        self.assertEqual(a_list.len(), len(temp_list1))
        self.assertEqual(b_list.len(), 1)
        self.assertEqual(c_list.len(), len(temp_list2))
        self.assertEqual(d_list.len(), 0)


class InsertHere(unittest.TestCase):

    def test_insert_func_returns_obj(self):
        a_list = LinkedList()
        b_list = LinkedList()
        c_list = LinkedList()
        d_list = LinkedList()

        temp_list1 = [1, 2]
        temp_list2 = [1, 2, 3, 4, 5]

        for j in temp_list2:
            c_list.add_in_tail(Node(j))
        for k in temp_list1:
            d_list.add_in_tail(Node(k))

        """Добавляем к пустому списку один узел."""

        n1 = Node(1)
        a_list.insert(None, n1)
        self.assertEqual(a_list.head, a_list.tail)
        self.assertEqual({'head': a_list.head, 'tail': a_list.tail}, a_list.__dict__)
        self.assertEqual(a_list.len(), 1)

        """Тест на проверку добавления в пустой список новый узел после не существующего узла."""

        n2 = Node('kjchv')
        a_list.clean()
        a_list.insert(n1, n2)
        self.assertEqual(a_list.len(), 0)
        self.assertEqual({'head': None, 'tail': None}, a_list.__dict__)
        self.assertEqual(a_list.head,  a_list.tail)

        """Добавляем к списку из одного узла уэел перед ним."""

        n3 = Node('3-')
        b_list.add_in_tail(Node('khkjbdvn'))
        b_list.insert(None, n3)
        self.assertEqual({'head': b_list.head, 'tail': b_list.tail}, b_list.__dict__)
        self.assertEqual(b_list.len(), 2)

        """Тест на добавление узла в конец списка."""

        def iter_list(c_list):

            """Функция принимает связанный список, а возвращает стандартный список узлов связанного списка."""

            node = c_list.head
            result = []
            while node is not None:
                result.append(node)
                node = node.next
            return result

        n4 = Node('r')
        c_list.insert(iter_list(c_list)[-1], n4)
        self.assertEqual(c_list.len(), 6)
        self.assertEqual(n4, c_list.tail)
        """Тест на добавление нового элемента в середину списка."""

        n5 = Node(117)
        c_list.insert(iter_list(c_list)[2], n5)
        self.assertEqual(c_list.len(), 7)
        self.assertEqual(n5, c_list.head.next.next.next)


