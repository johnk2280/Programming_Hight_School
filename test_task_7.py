from task_7 import *
import pytest
import random


@pytest.mark.parametrize('value1, value2, expected_result', [
    (0, 1, -1), (1, 1, 0), (2, 1, 1), (-10, -9, -1), (-10, -11, 1), (100, 0, 1), (0, 0, 0)
])
def test_compare(value1, value2, expected_result):
    o_list = OrderedList(True)
    assert o_list.compare(value1, value2) == expected_result


@pytest.mark.parametrize('range_limit', [1, 2, 3, 4, 5])
def test_add__ascending(range_limit):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    expected_result = []
    for i in range(range_limit):
        expected_result.append(o_list.find(i))

    assert o_list.get_all() == expected_result


@pytest.mark.parametrize('range_limit', [1, 2, 3, 4, 5])
def test_add__descending(range_limit):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    expected_result = []
    for i in range(range_limit - 1, -1, -1):
        expected_result.append(o_list.find(i))

    assert o_list.get_all() == expected_result


@pytest.mark.parametrize('range_limit, value, expected_result', [
    (1, 1, None), (0, 0, None), (10, 10, None), (10, -1, None)
])
def test_find__ascending__returns_none(range_limit, value, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.find(value) == expected_result


@pytest.mark.parametrize('range_limit, value, expected_result', [
    (1, 1, None), (0, 0, None), (10, 10, None), (10, 11, None)
])
def test_find__descending__returns_none(range_limit, value, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.find(value) == expected_result


@pytest.mark.parametrize('range_limit, value_head, value_tail', [(1, 0, 0), (10, 0, 9), (100, 0, 99)])
def test_find__ascending__returns_extreme_nodes(range_limit, value_head, value_tail):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.find(value_head) == o_list.head
    assert o_list.find(value_tail) == o_list.tail


@pytest.mark.parametrize('range_limit, value_head, value_tail', [(1, 0, 0), (10, 9, 0), (100, 99, 0)])
def test_find__descending__returns_extreme_nodes(range_limit, value_head, value_tail):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.find(value_head) == o_list.head
    assert o_list.find(value_tail) == o_list.tail


@pytest.mark.parametrize('range_limit, value', [(3, 1)])
def test_find__ascending__returns_inner_nodes(range_limit, value):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.find(value) == o_list.head.next
    assert o_list.find(value) == o_list.tail.prev


@pytest.mark.parametrize('range_limit, value', [(3, 1)])
def test_find__descending__returns_inner_nodes(range_limit, value):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.find(value) == o_list.head.next
    assert o_list.find(value) == o_list.tail.prev


@pytest.mark.parametrize('range_limit, item', [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)])
def test_delete__ascending(range_limit, item):
    o_list_1 = OrderedList(True)
    for i in range(range_limit):
        o_list_1.add(i)

    o_list_1.delete(item)
    expected_result = []
    for i in range(range_limit - 1):
        expected_result.append(o_list_1.find(i))

    assert o_list_1.get_all() == expected_result


@pytest.mark.parametrize('range_limit, item', [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)])
def test_delete__ascending(range_limit, item):
    o_list_1 = OrderedList(False)
    for i in range(range_limit):
        o_list_1.add(i)

    o_list_1.delete(item)
    expected_result = []
    for i in range(range_limit - 1):
        expected_result.append(o_list_1.find(i))

    assert o_list_1.get_all() == list(reversed(expected_result))


@pytest.mark.parametrize('range_limit, expected_result', [(1, 0), (10, 0), (1000, 0)])
def test_clean__ascending(range_limit, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    o_list.clean(False)
    assert o_list.len() == expected_result
    assert o_list.__dict__ == {'head': None, 'tail': None, '_OrderedList__ascending': False}


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 0), (10, 0), (1000, 0)])
def test_clean__descending(range_limit, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    o_list.clean(True)
    assert o_list.len() == expected_result
    assert o_list.__dict__ == {'head': None, 'tail': None, '_OrderedList__ascending': True}


@pytest.mark.parametrize('range_limit, item, expected_result', [(0, 1, 1), (1, 0, 2), (10, 3, 11), (1000, 500, 1001)])
def test_len_after_add__ascending(range_limit, item, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    o_list.add(item)
    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, item, expected_result', [(0, 1, 1), (1, 0, 2), (10, 3, 11), (1000, 500, 1001)])
def test_len_after_add__descending(range_limit, item, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    o_list.add(item)
    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (10, 3, 7), (1000, 999, 1), (100000, 100000, 0)
])
def test_len_after_delete_from_head__ascending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 1), (10, 3, 7), (1000, 999, 1), (1000, 1000, 1), (10000, 5000, 5000)
])
def test_len_after_delete_from_tail_and_center__ascending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit, 0, -1):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (10, 3, 6), (1000, 999, 0), (1000, 1000, 0), (10000, 5000, 4999)
])
def test_len_after_delete_from_head_and_center__descending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit, -1, -1):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (10, 3, 7), (1000, 999, 1), (1000, 1000, 0), (10000, 5000, 5000)
])
def test_len_after_delete_from_tail__descending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, item, expected_result', [(0, 1, 0), (1, 0, 0), (10, 3, 9), (1000, 500, 999)])
def test_len_after_add__ascending(range_limit, item, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    o_list.delete(item)
    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, item, expected_result', [(0, 1, 0), (1, 0, 0), (10, 3, 9), (1000, 500, 999)])
def test_len_after_add__descending(range_limit, item, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    o_list.delete(item)
    assert o_list.len() == expected_result


@pytest.mark.parametrize('string_1, string_2, expected_result', [
    ('a', 'a', 0), (' f', ' f ', 0), ('abc', 'abcde', -1), ('a b  c', 'abcde', 1)
])
def test_string_compare(string_1, string_2, expected_result):
    str_list = OrderedStringList(True)
    assert str_list.compare(string_1, string_2) == expected_result

