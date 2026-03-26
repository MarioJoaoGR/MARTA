
# Module: docstring_parser.tests.test_epydoc
from docstring_parser import parse
import pytest

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    docstring = parse(
        """
        Short description

        @meta: asd
            1
                2
            3
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta"]
    assert docstring.meta[0].description == "asd\n1\n    2\n3"

@pytest.mark.parametrize("docstring, expected_short_desc, expected_meta_count, expected_meta_arg, expected_meta_desc", [
    (
        """
        Another short description

        @meta: example
            1
                2
            3
        """,
        "Another short description",
        1,
        ["meta"],
        "example\n1\n    2\n3"
    ),
    (
        """
        Yet another short description

        @meta: test
            1
                2
            3
        """,
        "Yet another short description",
        1,
        ["meta"],
        "test\n1\n    2\n3"
    ),
])
def test_multiple_meta_descriptions(docstring, expected_short_desc, expected_meta_count, expected_meta_arg, expected_meta_desc):
    """Test parsing multiple meta documentation entries."""
    docstring = parse(docstring)
    assert docstring.short_description == expected_short_desc
    assert len(docstring.meta) == expected_meta_count
    if expected_meta_count > 0:
        assert docstring.meta[0].args == expected_meta_arg
        assert docstring.meta[0].description == expected_meta_desc
