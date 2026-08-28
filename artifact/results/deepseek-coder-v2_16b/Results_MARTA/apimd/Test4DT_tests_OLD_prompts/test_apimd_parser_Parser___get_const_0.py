
import pytest
from unittest.mock import patch, MagicMock
from apimd.parser import Parser


def test_missing_module():
    p = Parser()
    with patch('apimd.parser.Parser.parse', MagicMock(return_value=None)):
        with pytest.raises(Exception):
            p.get_const('some_module')