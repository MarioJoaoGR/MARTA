
import pytest
from unittest.mock import patch
from httpie.plugins.base import FormatterPlugin

def test_valid_input():
    formatter = FormatterPlugin(format_options={'indent': 4})
    
    # Test with a valid headers string
    headers = "Content-Type: text/html\nDate: Mon, 12 Jun 2023 18:30:52 GMT"
    formatted_headers = formatter.format_headers(headers)
    
    assert formatted_headers == headers
