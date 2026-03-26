
from typing import Any

import pytest


# Assuming ISortPrettyPrinter is defined somewhere in the module 'isort.literal'
class MyPrettyPrinter:
    def pformat(self, value: list[Any]) -> str:
        return ', '.join(map(str, sorted(value)))

printer = MyPrettyPrinter()

def test_valid_input():
    from isort.literal import _list
    
    result = _list([3, 1, 2], printer)
    assert result == "1, 2, 3"
