
import pytest

from isort._vendored.tomli._parser import Pos, parse_basic_str_escape


def test_none_input():
    with pytest.raises(TypeError):
        parse_basic_str_escape(None, Pos(0))
