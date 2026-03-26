
import pytest
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err
from isort._vendored.tomli._parser import Pos, ParseFloat, Flags, NestedDict

def test_none_input():
    with pytest.raises(TypeError):
        result = parse_inline_table(None, 0, float)
