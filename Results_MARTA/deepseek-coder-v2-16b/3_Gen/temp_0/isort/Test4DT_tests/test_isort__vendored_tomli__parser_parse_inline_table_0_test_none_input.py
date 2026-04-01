
import pytest

from isort._vendored.tomli._parser import (Flags, NestedDict, ParseFloat, Pos,
                                           parse_inline_table, suffixed_err)


def test_none_input():
    with pytest.raises(TypeError):
        result = parse_inline_table(None, 0, float)
