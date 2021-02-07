from task_1 import *


# Var 1
def sum_linked_lists_1(a_list, b_list):

    len_a = a_list.len()
    len_b = b_list.len()

    if len_a != len_b:
        return

    new_list = LinkedList()
    node_a = a_list.head
    node_b = b_list.head

    while node_a is not None:
        new_list.add_in_tail(Node(node_a.value + node_b.value))
        node_a, node_b = node_a.next, node_b.next

    return new_list


# Var 2
def sum_linked_lists_2(a_list, b_list):

    len_a = a_list.len()
    len_b = b_list.len()

    if len_a != len_b:
        return

    new_list = LinkedList()
    node_a = a_list.head
    node_b = b_list.head

    while node_a is not None:
        new_node = Node(node_a.value + node_b.value)
        if new_list.head is None:
            new_list.head = new_node
        else:
            new_list.tail.next = new_node
        new_list.tail = new_node
        node_a, node_b = node_a.next, node_b.next

    return new_list


#  Var 3
def sum_linked_lists_3(a_list, b_list):
    len_a = a_list.len()
    len_b = b_list.len()

    if len_a != len_b:
        return

    new_list = LinkedList()
    node_a = a_list.head
    node_b = b_list.head
    prev_val = 0

    while node_a is not None:
        val = node_a.value + node_b.value
        if new_list.head is None:
            new_list.insert(None, val)
        else:
            new_list.insert(prev_val, val)
        node_a, node_b = node_a.next, node_b.next
        prev_val = val

    return new_list

