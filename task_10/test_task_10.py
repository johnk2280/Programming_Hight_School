import pytest
from task_10 import PowerSet


@pytest.mark.parametrize('values, expected_result', [
    ([1, 2, 3, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 4, 5, 3], [1, 2, 3, 4, 5]),
])
def test_put(values, expected_result):
    ps = PowerSet()
    for value in values:
        ps.put(value)

    assert sorted(ps.slots) == expected_result


@pytest.mark.parametrize('values, value, expected_result', [
    ([1, 2, 3, 1, 2, 3], 2, True),
    ([1, 2, 3, 4, 5, 3], 15, False)
])
def test_get(values, value, expected_result):
    ps = PowerSet()
    for el in values:
        ps.put(el)

    assert ps.get(value) == expected_result


@pytest.mark.parametrize('values, value, expected_result', [
    ([1, 2, 3, 1, 2, 3], 2, True),
    ([1, 2, 3, 4, 5, 3], 15, False)
])
def test_remove(values, value, expected_result):
    ps = PowerSet()
    for el in values:
        ps.put(el)

    assert ps.remove(value) == expected_result


@pytest.mark.parametrize('values_1, values_2, expected_result', [
    ([1, 2, 3, 4, 5], [7, 8, 9, 2, 1], list({1, 2, 3, 4, 5} & {7, 8, 9, 2, 1})),
    ([1, 2, 3, 4, 5], [7, 8, 9], list({1, 2, 3, 4, 5} & {7, 8, 9})),
    ([1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4, 5], list({1, 2, 3, 4, 5} & {7, 8, 9, 1, 2, 3, 4, 5}))
])
def test_intersection(values_1, values_2, expected_result):
    ps1 = PowerSet()
    ps2 = PowerSet()
    for el in values_1:
        ps1.put(el)

    for el in values_2:
        ps2.put(el)

    assert ps1.intersection(ps2).slots == expected_result


@pytest.mark.parametrize('values_1, values_2, expected_result', [
    ([1, 2, 3, 4, 5], [7, 8, 9, 2, 1], [1, 2, 3, 4, 5, 7, 8, 9]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 7, 8, 9]),
])
def test_union(values_1, values_2, expected_result):
    ps1 = PowerSet()
    ps2 = PowerSet()
    for el in values_1:
        ps1.put(el)

    for el in values_2:
        ps2.put(el)

    assert ps1.union(ps2).slots == expected_result


@pytest.mark.parametrize('values_1, values_2, expected_result', [
    ([1, 2, 3, 4, 5], [7, 8, 9, 2, 1], [3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], []),
    ([1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4], [5]),
])
def test_difference(values_1, values_2, expected_result):
    ps1 = PowerSet()
    ps2 = PowerSet()
    for el in values_1:
        ps1.put(el)

    for el in values_2:
        ps2.put(el)

    assert ps1.difference(ps2).slots == expected_result


@pytest.mark.parametrize('values_1, values_2, expected_result', [
    ([1, 2, 3, 4, 5], [2, 1], True),
    ([1, 2, 3, 4, 5], [7, 8], False),
    ([1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4], False),
])
def test_issubset(values_1, values_2, expected_result):
    ps1 = PowerSet()
    ps2 = PowerSet()
    for el in values_1:
        ps1.put(el)

    for el in values_2:
        ps2.put(el)

    assert ps1.issubset(ps2) == expected_result
