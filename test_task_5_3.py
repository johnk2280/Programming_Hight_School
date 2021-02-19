from task_5_3 import *
from task_5 import *
import pytest


@pytest.mark.parametrize('range_limit, rotation_number, expected_result', [
    (5, 2, [2, 3, 4, 0, 1]), (5, 5, [0, 1, 2, 3, 4]), (5, 8, [3, 4, 0, 1, 2]), (5, 0, [0, 1, 2, 3, 4])
])
def test_scroll(range_limit, rotation_number, expected_result):
    q = Queue()
    for i in range(range_limit):
        q.enqueue(i)

    spam = scroll(q, rotation_number)
    assert [spam.dequeue() for _ in range(range_limit)] == expected_result


@pytest.mark.parametrize('range_limit, rotation_number, expected_result', [
    (5, 2, [2, 3, 4, 0, 1]), (5, 5, [0, 1, 2, 3, 4]), (5, 8, [3, 4, 0, 1, 2]), (5, 0, [0, 1, 2, 3, 4])
])
def test_size_after_scroll(range_limit, rotation_number, expected_result):
    q = Queue()
    for i in range(range_limit):
        q.enqueue(i)

    assert scroll(q, rotation_number).size() == range_limit

