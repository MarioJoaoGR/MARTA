
import pytest
from typing import Iterable

class Pos:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __add__(self, other):
        return Pos(self.value + 1)
    
    def __getitem__(self, index):
        if index >= len(src):
            raise IndexError
        return src[index]

def skip_chars(src: str, pos: Pos, chars: Iterable[str]) -> Pos:
    try:
        while src[pos.value] in chars:
            pos.value += 1
    except IndexError:
        pass
    return pos

@pytest.mark.parametrize("src, pos_val, chars", [("hello world", len("hello world") + 1, ["l"])])
def test_invalid_pos(src, pos_val, chars):
    with pytest.raises(IndexError):
        skip_chars(src, Pos(pos_val), chars)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_skip_chars_2_test_invalid_pos
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_2_test_invalid_pos.py:16:24: E0602: Undefined variable 'src' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_2_test_invalid_pos.py:18:15: E0602: Undefined variable 'src' (undefined-variable)


"""