
import pytest
from isort._vendored.tomli._parser import parse_array, skip_comments_and_array_ws

@pytest.mark.parametrize("src, expected", [
    ("[1, 2, 3]", ([1, 2, 3], 7)),
    ("[1.1, 2.2, 3.3]", ([1.1, 2.2, 3.3], 14)),
    ('["apple", "banana", "cherry"]', (["apple", "banana", "cherry"], 28))
])
def test_valid_case_2(src: str, expected: Tuple[list, int]):
    pos = 0
    parse_float = float if src.count('.') == 2 else None
    result = parse_array(src, pos, parse_float)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_array_3_test_valid_case_2
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_valid_case_2.py:10:42: E0602: Undefined variable 'Tuple' (undefined-variable)


"""