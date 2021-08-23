from task_3 import *
import pytest


@pytest.mark.parametrize('range_limit, index, item, expected_result', [
    (0, 0, '4', ['4']),
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
def test_array_count_after_insert__buffer_not_resized_1(range_limit, index, item, expected_result):
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
def test_array_count_after_insert__buffer_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(1, range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert a_arr.count == expected_result


@pytest.mark.parametrize('range_limit, index, item', [
    (0, 1, '4'), (10, -1, 10), (17, 18, 't'), (37, 60, 't'), (5, 6, 7)
])
def test_exception_after_insert(range_limit, index, item):
    a_arr = DynArray()
    for i in range(range_limit):
        a_arr.append(i)

    with pytest.raises(IndexError):
        assert a_arr.insert(index, item)


@pytest.mark.parametrize('range_limit, index, expected_result', [
    (1, 0, []), (2, 0, [1]), (2, 1, [0]), (3, 2, [0, 1]), (3, 0, [1, 2]), (16, 15, [i for i in range(15)]),
    (16, 0, [i for i in range(1, 16)]), (32, 31, [i for i in range(31)]), (64, 0, [i for i in range(1, 64)]),
    (128, 64, [i for i in range(64)] + [i for i in range(65, 128)])
])
def test_delete__buffer_not_resized(range_limit, index, expected_result):
    b_arr = DynArray()
    for i in range(range_limit):
        b_arr.append(i)

    b_arr.delete(index)
    assert [el for el in b_arr] == expected_result


@pytest.mark.parametrize('range_limit, index, expected_result', [
    (1, 0, 16), (2, 0, 16), (2, 1, 16), (3, 2, 16), (3, 0, 16), (16, 15, 16),
    (16, 0, 16), (32, 31, 32), (64, 0, 64), (128, 64, 128), (130, 54, 256), (270, 256, 512)
])
def test_buffer_capacity_after_delete__buffer_not_resized(range_limit, index, expected_result):
    b_arr = DynArray()
    for i in range(range_limit):
        b_arr.append(i)

    b_arr.delete(index)
    assert b_arr.capacity == expected_result


@pytest.mark.parametrize('range_limit, index, expected_result', [
    (1, 0, 0), (2, 0, 1), (2, 1, 1), (3, 2, 2), (3, 0, 2), (16, 15, 15),
    (16, 0, 15), (32, 31, 31), (64, 0, 63), (128, 64, 127), (130, 54, 129), (270, 256, 269)
])
def test_array_count_after_delete__buffer_not_resized(range_limit, index, expected_result):
    b_arr = DynArray()
    for i in range(range_limit):
        b_arr.append(i)

    b_arr.delete(index)
    assert b_arr.count == expected_result


@pytest.mark.parametrize('range_limit, index, expected_result', [
    (17, 0, [i for i in range(2, 17)]), (33, 20, [i for i in range(20)] + [i for i in range(22, 33)]),
    (65, 60, [i for i in range(60)] + [62, 63, 64]), (129, 100, [i for i in range(100)] + [i for i in range(102, 129)]),
    (257, 200, [i for i in range(200)] + [i for i in range(202, 257)])
])
def test_delete__buffer_resized(range_limit, index, expected_result):
    b_arr = DynArray()
    for i in range(range_limit):
        b_arr.append(i)

    b_arr.delete(index)
    b_arr.delete(index)
    assert [el for el in b_arr] == expected_result


@pytest.mark.parametrize('create_limit, delete_limit, expected_result', [
    (17, 2, 21), (17, 7, 16), (17, 10, 16), (1, 1, 16), (2, 1, 16), (3, 1, 16),
    (17, 5, 21), (33, 2, 42), (33, 13, 28), (33, 20, 18), (33, 25, 16),
    (65, 2, 85), (65, 23, 56), (65, 38, 37), (65, 47, 24), (65, 54, 16)])
def test_buffer_capacity_after_delete__buffer_resized(create_limit, delete_limit, expected_result):
    b_arr = DynArray()
    for i in range(create_limit):
        b_arr.append(i)

    for i in range(delete_limit):
        b_arr.delete(0)

    assert b_arr.capacity == expected_result


@pytest.mark.parametrize('range_limit, index, expected_result', [
    (17, 0, 15), (33, 20, 31), (65, 60, 63), (129, 100, 127), (257, 200, 255)
])
def test_array_count_after_delete__buffer_resized(range_limit, index, expected_result):
    b_arr = DynArray()
    for i in range(range_limit):
        b_arr.append(i)

    b_arr.delete(index)
    b_arr.delete(index)
    assert b_arr.count == expected_result


@pytest.mark.parametrize('range_limit, index', [(0,0), (10, -1), (17, 18), (37, 60), (5, 6)])
def test_exception_after_delete(range_limit, index):
    b_arr = DynArray()
    for i in range(range_limit):
        b_arr.append(i)

    with pytest.raises(IndexError):
        assert b_arr.delete(index)

