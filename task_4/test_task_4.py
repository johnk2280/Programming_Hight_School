from task_4 import *
import pytest


@pytest.mark.parametrize('range_limit, pop_limit, expected_result', [
    (0, 0, []), (0, 1, [None]), (1, 1, [0]), (2, 1, [1]), (120, 1, [119]), (10000, 1, [9999]),
    (2, 2, [1, 0]), (120, 10, [i for i in range(119, 109, -1)]), (10000, 100, [i for i in range(9999, 9899, -1)])
])
def test_push(range_limit, pop_limit, expected_result):
    spam = []
    a_stack = Stack()
    for i in range(range_limit):
        a_stack.push(i)

    for i in range(pop_limit):
        spam.append(a_stack.pop())

    assert spam == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 1), (2, 2), (120, 120), (10000, 10000)])
def test_size_after_push(range_limit, expected_result):
    s = Stack()
    for i in range(range_limit):
        s.push(i)

    assert s.size() == expected_result


@pytest.mark.parametrize('range_limit, pop_limit, expected_result', [
    (0, 0, None), (1, 1, 0), (2, 1, 1), (120, 10, 110), (120, 121, None), (10000, 1000, 9000), (10000, 10000, 0)
])
def test_pop(range_limit, pop_limit, expected_result):
    s = Stack()
    for i in range(range_limit):
        s.push(i)

    for j in range(pop_limit - 1):
        s.pop()

    assert s.pop() == expected_result


@pytest.mark.parametrize('range_limit, pop_limit, expected_result', [
    (0, 0, 0), (1, 1, 0), (2, 1, 1), (120, 10, 110), (120, 120, 0), (10000, 1000, 9000), (10000, 10000, 0)
])
def test_size_after_pop(range_limit, pop_limit, expected_result):
    s = Stack()
    for i in range(range_limit):
        s.push(i)

    for j in range(pop_limit):
        s.pop()

    assert s.size() == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, None), (1, 0), (2, 1), (120, 119), (10000, 9999)])
def test_peek(range_limit, expected_result):
    s = Stack()
    for i in range(range_limit):
        s.push(i)

    assert s.peek() == expected_result
