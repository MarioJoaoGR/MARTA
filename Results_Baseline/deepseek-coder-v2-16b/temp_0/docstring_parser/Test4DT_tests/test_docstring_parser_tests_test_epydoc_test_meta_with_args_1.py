
from docstring_parser import parse  # Assuming this function is defined elsewhere in your module or project
import pytest

def test_meta_with_args():
    """Test parsing meta with additional arguments."""
    docstring = parse(
        """
        Short description

        @meta ene due rabe: asd
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1