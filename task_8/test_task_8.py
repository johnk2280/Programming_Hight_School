import pytest

from task_8 import HashTable


@pytest.mark.parametrize('size, value, slot_index', [
    (17, 'Туча мглою небо кроетggggg', 7),
    (17, 'БаклажаН   ', 0),
    (17, 'Туча мглою небо кроет', 2),
    (17, 'Туча мглою небокроет', 4),
    (17, 'He666098766_!', 5),
    (17, 'Туча мглоюнебокроет', 6),
    (17, 'Тучамглоюнебокроет', 8),
    (17, 'тучамглоюнебокроет', 11),
    (17, 'Зимой и летом одним цветом', 12),
    (17, 'He6660)(*&^&%$#398__world_)wf4562245!', 13),
    (17, 'Зимой и летом однимцветом', 14),
    (17, 'Зимой и летомоднимцветом', 16),
    (17, 'Зимой илетомоднимцветом', 1),
    (17, 'Зимойилетомоднимцветом', 3),
    (17, 'Hello World!!@#$%^&*()', 15),
    (17, 'Hello World!&*(', 15),
    (17, 'Hello World!&*', 9),
    (17, 'HelWor___!', 10)
])
def test_hash_fun(size, value, slot_index):
    ht = HashTable(size, 2)
    assert ht.hash_fun(value) == slot_index


@pytest.mark.parametrize('size, value, slot_index', [
    (17, 'Туча мглою небо кроетggggg', 7),
    (17, 'БаклажаН   ', 0),
    (17, 'Туча мглою небо кроет', 2),
    (17, 'Туча мглою небокроет', 4),
    (17, 'He666098766_!', 5),
    (17, 'Туча мглоюнебокроет', 6),
    (17, 'Тучамглоюнебокроет', 8),
    (17, 'тучамглоюнебокроет', 11),
    (17, 'Зимой и летом одним цветом', 12),
    (17, 'He6660)(*&^&%$#398__world_)wf4562245!', 13),
    (17, 'Зимой и летом однимцветом', 14),
    (17, 'Зимой и летомоднимцветом', 16),
    (17, 'Зимой илетомоднимцветом', 1),
    (17, 'Зимойилетомоднимцветом', 3),
    (17, 'Hello World!!@#$%^&*()', 15),
    (17, 'Hello World!&*(', 15),
    (17, 'Hello World!&*', 9),
    (17, 'HelWor___!', 10)
])
def test_seek_slot(size, value, slot_index):
    ht = HashTable(size, 2)

    assert ht.seek_slot(value) == slot_index


@pytest.mark.parametrize('size, step, values, slot_indexes', [
    (17,
     8,
     [
         'Туча мглою небо кроетggggg',
         'Зимойилетомоднимцвто',
         'БаклажаН   ',
         'Туча мглою небо кроет',
         'Туча мглою небокроет',
         'He666098766_!',
         'Туча мглоюнебокроет',
         'Тучамглоюнебокроет',
         'тучамглоюнебокроет',
         'Зимой и летом одним цветом',
         'He6660)(*&^&%$#398__world_)wf4562245!',
         'Зимой и летом однимцветом',
         'Зимой и летомоднимцветом',
         'Зимой илетомоднимцветом',
         'Зимойилетомоднимцветом',
         'Hello World!!@#$%^&*()',
         'Hello World!&*',
         'HelWor___!',
         'Hello World!&*(',
         'Зимойилетомоднимцвето'
     ],
     [7, 0, 0, 2, 4, 5, 6, 8, 11, 12, 13, 14, 16, 1, 3, 15, 9, 10, 15, 15])
])
def test_seek_slot_after_filling(size, step, values, slot_indexes):
    ht = HashTable(size, step)
    result = []
    for i in range(len(values)):
        result.append(ht.seek_slot(values[i]))

    assert result == slot_indexes


@pytest.mark.parametrize('size, step, values, slots', [
    (17,
     8,
     [
         'Помидор',
         'Баклажан',
         'Огурец',
         'Свекла',
         'Картофель',
         'Лук',
         'Апельсин',
         'Яблоко',
         'Банан',
         'Вишня',
         'Салат',
         'Морковь',
         'Груша',
         'Манго',
         'Мандарин',
         'Арбуз',
         'Дыня',
         'Сельдерей',
         'Земляника'
     ],
     [
         'Манго',
         'Салат',
         'Апельсин',
         'Огурец',
         'Баклажан',
         'Свекла',
         'Арбуз',
         'Помидор',
         'Морковь',
         'Лук',
         'Груша',
         'Банан',
         'Вишня',
         'Картофель',
         'Дыня',
         'Яблоко',
         'Мандарин'])
])
def test_put(size, step, values, slots):
    ht = HashTable(size, step)
    for i in range(len(values)):
        ht.put(values[i])

    assert ht.slots == slots


@pytest.mark.parametrize('size, step, values, expected_result', [
    (17,
     8,
     [
         'Помидор',
         'Баклажан',
         'Огурец',
         'Свекла',
         'Картофель',
         'Лук',
         'Апельсин',
         'Яблоко',
         'Банан',
         'Вишня',
         'Салат',
         'Морковь',
         'Груша',
         'Манго',
         'Мандарин',
         'Арбуз',
         'Дыня',
         'Сельдерей',
         'Земляника'
     ],
     [7, 4, 3, 5, 13, 9, 2, 15, 11, 12, 1, 8, 10, 0, 16, 6, 14, None, None])
])
def test_find(size, step, values, expected_result):
    ht = HashTable(size, step)
    result = []
    for i in range(len(values)):
        ht.put(values[i])

    for i in range(len(values)):
        result.append(ht.find(values[i]))

    assert result == expected_result
