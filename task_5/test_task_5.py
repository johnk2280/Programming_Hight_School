from task_5 import *
import pytest


@pytest.mark.parametrize('start, finish, expected_result', [(2, 5, 2), (0, 2, 0), (1, 2, 1), (5, 9, 5)])
def test_enqueue(start, finish, expected_result):
    q = Queue()
    for i in range(start, finish):
        q.enqueue(i)
    assert q.dequeue() == expected_result


@pytest.mark.parametrize('start, finish, dif, expected_result', [
    (2, 5, 1, 4), (0, 2, 1, 1), (1, 2, 0, None), (5, 9, 2, 7)])
def test_dequeue(start, finish, dif, expected_result):
    q = Queue()
    for i in range(start, finish):
        q.enqueue(i)
    for i in range(start, finish - dif):
        q.dequeue()
    assert q.dequeue() == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(1, 1), (0, 0), (1000, 1000), (5, 5)])
def test_size(range_limit, expected_result):
    q = Queue()
    for i in range(range_limit):
        q.enqueue(i)
    assert q.size() == expected_result

