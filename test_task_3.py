from task_3 import *
import pytest


@pytest.mark.parametrize('range_limit, index, item, expected_result', [
    (10, 3, 117, [0, 1, 2, 117, 3, 4, 5, 6, 7, 8, 9]),
    (11, 10, '16', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '16', 10]),
    (12, 12, '12', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, '12']),
    (13, 0, None, [None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    (14, 7, False, [0, 1, 2, 3, 4, 5, 6, False, 7, 8, 9, 10, 11, 12, 13]),
    (15, 15, True, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, True])
])
def test_insert__buffer_not_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert [el for el in a_arr] == expected_result


@pytest.mark.parametrize('range_limit, index, item, expected_result', [(10, 3, 117, 16), (11, 10, '16', 16),
                                                                       (12, 12, '12', 16), (13, 0, None, 16),
                                                                       (14, 7, False, 16), (15, 15, True, 16)])
def test_buffer_capacity_after_insert__buffer_not_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert a_arr.capacity == expected_result


@pytest.mark.parametrize('range_limit, index, item, expected_result', [(10, 3, 117, 11), (11, 10, '16', 12),
                                                                       (12, 12, '12', 13), (13, 0, None, 14),
                                                                       (14, 7, False, 15), (15, 15, True, 16)])
def test_count_array_after_insert__buffer_not_resized_1(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert a_arr.count == expected_result


@pytest.mark.parametrize('range_limit, index, item, expected_result', [
    (17, 3, 117, [1, 2, 3, 117] + [i for i in range(4, 17)]),
    (18, 10, '16', [i for i in range(1, 11)] + ['16'] + [i for i in range(11, 18)]),
    (19, 12, '12', [i for i in range(1, 13)] + ['12'] + [i for i in range(13, 19)]),
    (20, 0, None, [None] + [i for i in range(1, 20)]),
    (21, 7, False, [i for i in range(1, 8)] + [False] + [i for i in range(8, 21)]),
    (22, 16, True, [i for i in range(1, 17)] + [True] + [i for i in range(17, 22)]),
    (65, 64, 0.5, [i for i in range(1, 65)] + [0.5])
])
def test_insert__buffer_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(1, range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert [el for el in a_arr] == expected_result


@pytest.mark.parametrize('range_limit, index, item, expected_result', [(17, 16, 1, 32), (65, 17, 1, 128),
                                                                       (129, 17, 1, 256), (257, 17, 1, 512)])
def test_buffer_capacity_after_insert__buffer_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(1, range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert a_arr.capacity == expected_result


@pytest.mark.parametrize('range_limit, index, item, expected_result', [(17, 16, 1, 17), (65, 17, 1, 65),
                                                                       (129, 17, 1, 129), (257, 17, 1, 257)])
def test_count_array_after_insert__buffer_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(1, range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert a_arr.count == expected_result


@pytest.mark.parametrize('range_limit, index, item', [(10, -1, 10), (17, 18, 't'),
                                                      (37, 60, 't'), (5, 6, 7)])
def test_exception_after_insert(range_limit, index, item):
    a_arr = DynArray()
    for i in range(range_limit):
        a_arr.append(i)

    with pytest.raises(IndexError):
        assert a_arr.insert(index, item)



