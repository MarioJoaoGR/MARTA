
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.base import FormatterPlugin

def test_valid_input():
    with patch('httpie.plugins.base.FormatterPlugin.__init__', return_value=None):
        formatter = FormatterPlugin(format_options={'indent': 4})
        assert formatter.format_body("some text", "text/plain") == "some text"
