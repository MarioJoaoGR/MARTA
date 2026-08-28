
import pytest
from thonny.roughparse import _build_char_in_string_func, _is_char_in_string


def test_edge_case_none():
    build_func = _build_char_in_string_func(None)
    with pytest.raises(TypeError):
        check_character = build_func(10)  # This should raise TypeError because startindex is None