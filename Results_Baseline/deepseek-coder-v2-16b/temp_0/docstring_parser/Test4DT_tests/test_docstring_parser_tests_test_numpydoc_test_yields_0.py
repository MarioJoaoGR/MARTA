
# Module: docstring_parser.tests.test_numpydoc
# Import the function from its module
from docstring_parser.tests.test_numpydoc import test_yields

def test_parse():
    # Test case for parsing a docstring with a 'Yields' section
    from docstring_parser import parse  # Corrected the import and variable usage

    docstring = parse(
        """
        Short description
        Yields
        ------
        int
            description
        """
    )
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["yields"]
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[0].description == "description"
    assert docstring.meta[0].return_name is None
    assert docstring.meta[0].is_generator
