
import pytest
from apimd.parser import Parser

def test_compile_no_data():
    p = Parser()
    result = p.compile()
    assert result == "\n"





