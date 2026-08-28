
import pytest
from unittest.mock import patch
from youtube_dl.downloader.f4m import _add_ns

@pytest.mark.parametrize("input_prop, expected", [('title', "{http://ns.adobe.com/f4m/1.0}title")])
def test_valid_input_default_version(input_prop, expected):
    with patch('__main__._add_ns') as mock_add_ns:
        result = _add_ns(input_prop)
        assert result == expected

@pytest.mark.parametrize("input_prop, ver, expected", [('description', 2, "{http://ns.adobe.com/f4m/2.0}description')])
def test_valid_input_specified_version(input_prop, ver, expected):
    with patch('__main__._add_ns') as mock_add_ns:
        result = _add_ns(input_prop, ver)
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: unterminated string literal (detected at line 12) (line 12, col 75)
@pytest.mark.parametrize("input_prop, ver, expected", [('description', 2, "{http://ns.adobe.com/f4m/2.0}description')])
"""