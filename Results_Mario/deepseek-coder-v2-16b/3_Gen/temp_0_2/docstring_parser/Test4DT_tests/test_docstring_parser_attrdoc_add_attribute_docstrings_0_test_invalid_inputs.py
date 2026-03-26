
import pytest
from types import ModuleType
import typing as T  # Renaming for clarity
from docstring_parser.attrdoc import add_attribute_docstrings, Docstring

def test_invalid_inputs():
    # Test with invalid types for obj and docstring
    with pytest.raises(AttributeError):
        add_attribute_docstrings('invalid', 1234)
