
import pytest
from unittest.mock import patch
from httpie.plugins.base import FormatterPlugin

def test_edge_case_none():
    with patch('httpie.plugins.base.FormatterPlugin.__init__', return_value=None):
        formatter = FormatterPlugin(format_options={'indent': 4})
        assert formatter.format_headers("Content-Type: text/html\nDate: Mon, 12 Jun 2023 18:30:52 GMT") == "Content-Type: text/html\nDate: Mon, 12 Jun 2023 18:30:52 GMT"
