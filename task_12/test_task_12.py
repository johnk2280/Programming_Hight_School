import pytest
from task_12 import NativeCache


@pytest.mark.parametrize('size, items, slots, values', [
    (
            5,
            [('Помидор', 12), ('Баклажан', 1), ('Огурец', 4), ('Свекла', 6), ('Картофель', 10)],
            ['Баклажан', 'Помидор', 'Огурец', 'Картофель', 'Свекла'],
            [1, 12, 4, 10, 6]
    ),
])
def test_put_insert_new_values(size, items, slots, values):
    nc = NativeCache(size)
    for i in range(size):
        nc.put(items[i][0], items[i][1])

    assert nc.slots == slots
    assert nc.values == values


@pytest.mark.parametrize('size, items, slots, values', [
    (
            5,
            [('Помидор', 12), ('Баклажан', 1), ('Огурец', 4), ('Свекла', 6), ('Картофель', 10)],
            ['Баклажан', 'Помидор', 'Огурец', 'Картофель', 'Свекла'],
            [25, 5, 15, 10, 6]
    ),
])
def test_put_update_values(size, items, slots, values):
    nc = NativeCache(size)
    for i in range(size):
        nc.put(items[i][0], items[i][1])

    nc.put('Баклажан', 25)
    nc.put('Помидор', 5)
    nc.put('Огурец', 15)

    assert nc.slots == slots
    assert nc.values == values


@pytest.mark.parametrize('size, items, keys, expected_result', [
    (
            5,
            [('Помидор', 12), ('Баклажан', 1), ('Огурец', 4), ('Свекла', 6), ('Картофель', 10)],
            ['Помидор', 'Балаклава', 'рец', 'Свекла', 'Картофель'],
            [True, False, False, True, True]
    )
])
def test_is_key(size, items, keys, expected_result):
    nc = NativeCache(size)
    result = []
    for i in range(size):
        nc.put(items[i][0], items[i][1])

    for i in range(size):
        result.append(nc.is_key(keys[i]))

    assert result == expected_result


@pytest.mark.parametrize('size, items, keys, expected_result', [
    (
            5,
            [('Помидор', 12), ('Баклажан', 1), ('Огурец', 4), ('Свекла', 6), ('Картофель', 10)],
            ['омидор', 'Балаклава', 'рец', 'Свекла', 'Картофель'],
            [None, None, None, 6, 10]
    )
])
def test_get(size, items, keys, expected_result):
    nc = NativeCache(size)
    result = []
    for i in range(size):
        nc.put(items[i][0], items[i][1])

    for i in range(size):
        result.append(nc.get(keys[i]))

    assert result == expected_result
