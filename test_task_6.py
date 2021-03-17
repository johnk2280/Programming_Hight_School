import pytest
from task_6 import *


def test_removeTail_empty_deque():
    a_deque = Deque()
    assert a_deque.removeTail() is None


def test_removeFront_empty_deque():
    a_deque = Deque()
    assert a_deque.removeFront() is None


@pytest.mark.parametrize('range_limit, remove_limit, item, expected_result', [
    (1, 2, '0', [0, '0']), (5, 6, 1, [0, 1, 2, 3, 4, 1]), (2, 3, [True], [0, 1, [True]]),
    (10000, 10001, 100, [i for i in range(10000)] + [100]), (1, 3, True, [0, True, None])
])
def test_addTail(range_limit, remove_limit, item, expected_result):
    spam = []
    a_deque = Deque()
    for i in range(range_limit):
        a_deque.addTail(i)

    a_deque.addTail(item)
    for i in range(remove_limit):
        spam.append(a_deque.removeFront())

    assert spam == expected_result


@pytest.mark.parametrize('range_limit, remove_limit, item, expected_result', [
    (1, 2, '0', [0, '0']), (5, 6, 1, [0, 1, 2, 3, 4, 1]), (2, 3, [True], [0, 1, [True]]),
    (10000, 10001, 100, [i for i in range(10000)] + [100]), (1, 3, True, [0, True, None])
])
def test_addFront(range_limit, remove_limit, item, expected_result):
    spam = []
    a_deque = Deque()
    for i in range(range_limit):
        a_deque.addFront(i)

    a_deque.addFront(item)
    for i in range(remove_limit):
        spam.append(a_deque.removeTail())

    assert spam == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 1), (5, 5), (1000, 1000)])
def test_size_after_addFront(range_limit, expected_result):
    a_deque = Deque()
    for i in range(range_limit):
        a_deque.addFront(i)

    assert a_deque.size() == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 1), (5, 5), (1000, 1000)])
def test_size_after_addTail(range_limit, expected_result):
    a_deque = Deque()
    for i in range(range_limit):
        a_deque.addTail(i)

    assert a_deque.size() == expected_result


@pytest.mark.parametrize('range_limit, remove_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (5, 2, 3), (1000, 100, 900), (10000, 9999, 1)
])
def test_size_after_removeFront(range_limit, remove_limit, expected_result):
    a_deque = Deque()
    for i in range(range_limit):
        a_deque.addFront(i)

    for i in range(remove_limit):
        a_deque.removeFront()

    assert a_deque.size() == expected_result


@pytest.mark.parametrize('range_limit, remove_limit, expected_result', [
    (0, 1, 0), (1, 1, 0), (5, 2, 3), (1000, 100, 900), (10000, 9999, 1)
])
def test_size_after_removeTail(range_limit, remove_limit, expected_result):
    a_deque = Deque()
    for i in range(range_limit):
        a_deque.addTail(i)

    for j in range(remove_limit):
        a_deque.removeTail()

    assert a_deque.size() == expected_result


