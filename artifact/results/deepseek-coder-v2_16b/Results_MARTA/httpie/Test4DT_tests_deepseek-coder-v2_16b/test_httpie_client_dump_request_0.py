
import pytest
from httpie.client import dump_request
import sys
import io
from unittest.mock import patch

def repr_dict(d):
    return dict(**{f"'{k}': {v!r}" for k, v in d.items()})

def test_valid_input():
    kwargs = {'method': 'GET', 'url': 'https://api.example.com/data'}
    with patch('sys.stderr', new=io.StringIO()) as mock_stderr:
        dump_request(kwargs)
        output = mock_stderr.getvalue().strip()
        assert ">>> requests.request(**" in output, f"Expected 'requests.request(**' in stderr output, but got {output}"
        assert "'method': 'GET'" in output, f"Expected 'method': 'GET' in stderr output, but got {output}"
        assert "'url': 'https://api.example.com/data'" in output, f"Expected 'url': 'https://api.example.com/data' in stderr output, but got {output}"

