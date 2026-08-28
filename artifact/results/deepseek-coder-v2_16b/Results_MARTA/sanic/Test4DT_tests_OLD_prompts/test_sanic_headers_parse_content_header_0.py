
import pytest
from unittest.mock import patch, MagicMock
from sanic.headers import parse_content_header
from typing import Tuple, Dict, Union

def test_parse_valid_content_header():
    with patch('sanic.headers.parse_content_header', MagicMock(return_value=('form-data', {'name': 'upload', 'filename': 'file.txt'}))):
        value = 'form-data; name=upload; filename="file.txt"'
        result = parse_content_header(value)
        assert result == ('form-data', {'name': 'upload', 'filename': 'file.txt'})
