import pytest
from task_4_6 import *


@pytest.mark.parametrize('polish_notation, expected_result', [
    ('8 2 + 5 * 9 + =', 59), ('7 2 3 * -', 1), ('10 15 - 3 *', -15), ('3 10 15 - *', -15), ('5 2 * 10 +', 20),
    ('5 2 * 10 + 1', 'Invalid notation')
])
def test_get_result_ok(polish_notation, expected_result):
    assert get_result(polish_notation) == expected_result


@pytest.mark.parametrize('polish_notation', [
    '8 2 + 5 * 9 + v =', '! 7 2 3 * -', '10 15 -- 3 *', '3 10! 15 - *', '5 u 2 * 10 +'
])
def test_get_result_exception(polish_notation):
    with pytest.raises(ValueError):
        assert get_result(polish_notation)
