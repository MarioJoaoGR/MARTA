
# Module: docstring_parser.tests.test_epydoc
# test_epydoc.py
from docstring_parser import parse  # Assuming this function is defined elsewhere in your module or project

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
    assert docstring.meta[0].args == ["meta", "ene", "due", "rabe"]
    assert docstring.meta[0].description == "asd"
