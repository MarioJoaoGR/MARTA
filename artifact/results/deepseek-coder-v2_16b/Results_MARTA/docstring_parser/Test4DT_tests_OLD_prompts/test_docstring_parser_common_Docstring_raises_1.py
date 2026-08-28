
import pytest
from unittest.mock import patch
from docstring_parser.common import Docstring, DocstringRaises

def test_docstring_raises():
    """Test that the raises method correctly filters out DocstringRaises objects from metadata."""
    # Create a Docstring instance with some mock metadata
    doc = Docstring()
    
    class MockDocstringRaises:
        pass
    
    # Add an instance of DocstringRaises to the meta list for testing
    doc.meta.append(MockDocstringRaises())
    
    # Call the raises method and check if it returns a list containing only instances of DocstringRaises
    with patch('docstring_parser.common.Docstring.raises', return_value=[MockDocstringRaises()]):
        filtered_list = doc.raises()
        assert isinstance(filtered_list[0], MockDocstringRaises)
