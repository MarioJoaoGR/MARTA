
import pytest
from docstring_parser.common import DocstringMeta

def test_edge_cases():
    # Test initialization with edge cases
    meta = DocstringMeta([], None)
    assert meta.args == []
    assert meta.description is None

    meta = DocstringMeta(['arg1', 'arg2'], "Description of args")
    assert meta.args == ['arg1', 'arg2']
    assert meta.description == "Description of args"
