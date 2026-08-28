
import pytest
from unittest.mock import patch
from tornado.escape import xhtml_escape, _XHTML_ESCAPE_DICT

def test_xhtml_escape_basic():
    # Test basic functionality with a string containing an ampersand entity
    assert xhtml_escape("Hello, &") == "Hello, &amp;"

@patch('tornado.escape._XHTML_ESCAPE_DICT', {'<': '&lt;', '>': '&gt;', '"': '&quot;', "'": "&#39;", '&': '&amp;'})
def test_xhtml_escape_mocked():
    # Test with the mocked escape dictionary
    assert xhtml_escape("Hello, <World>!") == "Hello, &lt;World&gt;!"

def test_xhtml_escape_attributes():
    # Test escaping for use in HTML attributes
    assert xhtml_escape('value="test"') == 'value=&quot;test&quot;'
