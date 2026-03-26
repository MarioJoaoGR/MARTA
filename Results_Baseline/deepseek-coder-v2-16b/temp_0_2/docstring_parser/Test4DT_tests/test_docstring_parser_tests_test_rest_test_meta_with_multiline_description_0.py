# Module: docstring_parser.tests.test_rest
import pytest
from docstring_parser import parse

def test_meta_with_multiline_description():
    """Test parsing multiline meta documentation."""
    docstring = parse(
        """
        Short description

        :meta: asd
            1
                2
            3
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    meta_entry = docstring.meta[0]
    assert meta_entry.args == ["meta"]
    assert meta_entry.description == "asd\n1\n    2\n3"

# Additional test cases can be added to cover different scenarios or edge cases
