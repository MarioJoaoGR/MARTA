
from unittest.mock import patch
import pytest
from thonny.roughparse import RoughParser


def test_invalid_input():
    with pytest.raises(ValueError):
        with patch('thonny.roughparse.RoughParser.__init__', side_effect=ValueError("Test ValueError")):
            RoughParser(indent_width=4, tabwidth=4)