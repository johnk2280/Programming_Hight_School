import pytest
from task_11 import BloomFilter


@pytest.mark.parametrize('string, hash1, hash2', [
    ('0123456789', 13, 5),
    ('1234567890', 29, 27),
    ('2345678901', 13, 5),
    ('3456789012', 29, 27),
    ('4567890123', 13, 5),
    ('5678901234', 29, 27),
    ('6789012345', 13, 5),
    ('7890123456', 29, 27),
    ('8901234567', 13, 5),
    ('9012345678', 29, 27)
])
def test_hash1(string, hash1, hash2):
    bf = BloomFilter(32)

    assert bf.hash1(string) == hash1
    assert bf.hash2(string) == hash2


@pytest.mark.parametrize('strings, string, expected_result', [
    ([
         '0123456789',
         '1234567890',
         '2345678901',
         '3456789012',
         '4567890123',
         '5678901234',
         '6789012345',
         '7890123456',
         '8901234567',
         '9012345678'
     ],
     '0123456789',
     True
    )
])
def test_is_value(strings, string, expected_result):
    bf = BloomFilter(32)
    for el in strings:
        bf.add(el)

    assert bf.is_value(string) == expected_result
