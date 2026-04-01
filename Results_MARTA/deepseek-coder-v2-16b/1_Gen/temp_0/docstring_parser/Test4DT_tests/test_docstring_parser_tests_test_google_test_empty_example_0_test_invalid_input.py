
import pytest
from docstring_parser.tests.test_google import parse

def test_empty_example() -> None:
    """Test parsing empty examples section."""
    docstring = parse(
        """Short description

        Example:

        Raises:
            IOError: some error
        """
    )

    assert len(docstring.examples) == 1
    assert docstring.examples[0].args == ["examples"]
    assert docstring.examples[0].description == ""
