
import pytest
from unittest.mock import patch
from thonny.roughparse import _is_char_in_string


def test_edge_case_none():
    with pytest.raises(TypeError):
        _is_char_in_string()
