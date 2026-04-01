
import pytest
from isort.literal import ISortPrettyPrinter
from typing import Any

def _unique_tuple(value: tuple[Any, ...], printer: ISortPrettyPrinter) -> str:
    return printer.pformat(tuple(sorted(set(value))))

def test_invalid_input():
    class MyMockPrettyPrinter:
        def pformat(self, value: Any) -> str:
            if value is None:
                return "None"
            else:
                return ', '.join(map(str, value))
    
    with pytest.raises(TypeError):
        _unique_tuple(None, MyMockPrettyPrinter())
