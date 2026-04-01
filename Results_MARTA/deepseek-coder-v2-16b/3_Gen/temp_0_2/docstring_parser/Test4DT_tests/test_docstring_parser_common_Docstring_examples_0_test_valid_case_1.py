
import pytest
from docstring_parser.common import Docstring  # Assuming this is the correct module path

def test_valid_case_1():
    # Create a mock for DocstringStyle if necessary, otherwise remove the style parameter from the constructor call
    class MockDocstringStyle:
        def __init__(self, style=None):
            self.style = style
    
    doc = Docstring(style=MockDocstringStyle("custom"))
    assert doc.style is not None
    assert doc.style.style == "custom"
