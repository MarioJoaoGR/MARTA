
import pytest
from unittest.mock import patch, MagicMock
from apimd.parser import Parser


def test_invalid_input():
    with pytest.raises(TypeError):
        p = Parser(link=True, level=1)
        p.parse('test_pkg_name', "Invalid content")  # Should raise ValueError for invalid content