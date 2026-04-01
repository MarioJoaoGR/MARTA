
import warnings
from docstring_parser.tests.test_numpydoc import parse

def test_warns() -> None:
    """Test parsing warns."""
    with warnings.catch_warnings(record=True) as w:
        # Trigger a warning
        warnings.simplefilter("always")
        docstring = parse(
            """
            Short description
            Warns
            -----
            UserWarning
                description
            """
        )
        
        # Check that exactly one warning was raised and it is of type UserWarning with the specified description
        assert len(docstring.meta) == 1, "Expected exactly one warning"
        assert isinstance(docstring.meta[0].type_name, str), "Expected a string for warning type"
        assert docstring.meta[0].type_name == "UserWarning", f"Unexpected warning type: {docstring.meta[0].type_name}"
        assert isinstance(docstring.meta[0].description, str), "Expected a string for warning description"
        assert docstring.meta[0].description == "description", f"Unexpected warning description: {docstring.meta[0].description}"
