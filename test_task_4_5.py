from task_4_5 import *
import pytest


@pytest.mark.parametrize('string, expected_result', [
    ('(()()()((()', False), ('(()()()((()))))', False), (')(()()()((()', False), ('(()()()((())))', True),
    ('()()()()', True), (')((()', False), ('()))((()', False), ('(()()())((()))', True),
    ('(some) 76090(words) and (simbols&%&$^%)', True), ('()', True), (')(', False), ('()))((', False)
])
def test_check_balance(string, expected_result):
    assert check_balance(string) == expected_result

