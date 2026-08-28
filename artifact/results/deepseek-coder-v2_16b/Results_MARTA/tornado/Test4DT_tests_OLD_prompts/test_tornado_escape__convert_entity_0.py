
import pytest
import re
import typing
from unittest.mock import patch
from tornado.escape import _convert_entity, _HTML_UNICODE_MAP

def test_valid_input():
    @pytest.mark.parametrize("input_str, expected", [
        ('&amp;', '&'),
        ('&#160;', ' '),  # Non-breaking space
        ('&#x8F;', '')   # Black non-scanned
    ])
    def test_valid_input(input_str, expected):
        match = re.match(r'(&#(\d+)|#(\d{1,5})|([a-zA-Z]+));', input_str)
        assert _convert_entity(match) == expected

def test_invalid_input():
    @pytest.mark.parametrize("input_str", [None, ''])
    def test_invalid_input(input_str):
        match = re.match(r'(&#(\d+)|#(\d{1,5})|([a-zA-Z]+));', input_str) if input_str else None
        with pytest.raises(TypeError):
            _convert_entity(match)

def test_none_input():
    @pytest.mark.parametrize("input_str", [None, ''])
    def test_none_input(input_str):
        match = re.match(r'(&#(\d+)|#(\d{1,5})|([a-zA-Z]+));', input_str) if input_str else None
        with pytest.raises(TypeError):
            _convert_entity(match)

def test_empty_input():
    @pytest.mark.parametrize("input_str", [None, ''])
    def test_empty_input(input_str):
        match = re.match(r'(&#(\d+)|#(\d{1,5})|([a-zA-Z]+));', input_str) if input_str else None
        with pytest.raises(TypeError):
            _convert_entity(match)
