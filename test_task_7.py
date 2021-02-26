from task_7 import *
import pytest
import random


@pytest.mark.parametrize()
def test_compare():
    pass


@pytest.mark.parametrize()
def test_add():
    # учесть параметр asc
    pass


@pytest.mark.parametrize()
def test_find():
    pass


@pytest.mark.parametrize('range_limit, item, expected_result', [
    (0, 1, []), (1, 1, [0]), (10, 3, [0, 1, 2, 4, 5, 6, 7, 8, 9]),
    (1000, 500, [i for i in range(500)] + [i for i in range(501, 1000)]),
    (1000, 1000, [i for i in range(1000)]), (100000, 99999, [i for i in range(99999)]),
    (100000, 50000, [i for i in range(50000)] + [i for i in range(50001, 100000)])
])
def test_delete__ascending(range_limit, item, expected_result):
    o_list_1 = OrderedList(True)
    for i in range(range_limit):
        o_list_1.add(i)

    assert o_list_1.delete(item) == expected_result


@pytest.mark.parametrize('range_limit, item, expected_result', [
    (0, 1, []), (1, 1, [0]), (10, 3, list(reversed([0, 1, 2, 4, 5, 6, 7, 8, 9]))),
    (1000, 500, list(reversed([i for i in range(500)] + [i for i in range(501, 1000)]))),
    (1000, 1000, list(reversed([i for i in range(1000)]))), (100000, 99999, list(reversed([i for i in range(99999)]))),
    (100000, 50000, list(reversed([i for i in range(50000)] + [i for i in range(50001, 100000)])))
])
def test_delete__descending(range_limit, item, expected_result):
    o_list_1 = OrderedList(False)
    for i in range(range_limit):
        o_list_1.add(i)

    assert o_list_1.delete(item) == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 0), (10, 0), (1000, 0), (100000, 0)])
def test_clean__ascending(range_limit, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.clean(False).len() == expected_result
    assert o_list.__dict__ == {'head': None, 'tail': None, '_OrderedList__ascending': False}


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 0), (10, 0), (1000, 0), (100000, 0)])
def test_clean__descending(range_limit, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    assert o_list.clean(True).len() == expected_result
    assert o_list.__dict__ == {'head': None, 'tail': None, '_OrderedList__ascending': True}


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 1), (10, 10), (1000, 1000), (100000, 100000)])
def test_len_after_add__ascending(range_limit, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(random.randint(0, range_limit if range_limit < 10 else range_limit / 10))

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 1), (10, 10), (1000, 1000), (100000, 100000)])
def test_len_after_add__descending(range_limit, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(random.randint(0, range_limit if range_limit < 10 else range_limit / 10))

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (10, 3, 7), (1000, 999, 1), (100000, 100000, 0), (100000, 50000, 50000)
])
def test_len_after_delete_from_head__ascending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (10, 3, 7), (1000, 999, 1), (1000, 1000, 0), (100000, 100000, 0), (100000, 50000, 50000)
])
def test_len_after_delete_from_tail_and_center__ascending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(True)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit, -1, -1):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (10, 3, 7), (1000, 999, 1), (1000, 1000, 0), (100000, 100000, 0), (100000, 50000, 50000)
])
def test_len_after_delete_from_head_and_center__descending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit, -1, -1):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize('range_limit, removal_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (10, 3, 7), (1000, 999, 1), (1000, 1000, 0), (100000, 100000, 0), (100000, 50000, 50000)
])
def test_len_after_delete_from_tail__descending(range_limit, removal_limit, expected_result):
    o_list = OrderedList(False)
    for i in range(range_limit):
        o_list.add(i)

    for i in range(removal_limit):
        o_list.delete(i)

    assert o_list.len() == expected_result


@pytest.mark.parametrize()
def test_string_compare():
    pass

























