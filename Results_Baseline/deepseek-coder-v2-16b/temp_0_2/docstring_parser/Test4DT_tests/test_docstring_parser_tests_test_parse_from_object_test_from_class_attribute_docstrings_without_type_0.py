# Module: docstring_parser.tests.test_parse_from_object
# Import the function correctly using its module name
from docstring_parser.tests.test_parse_from_object import parse_from_object

def test_from_class_attribute_docstrings_without_type():
    """Test the parsing of untyped attribute docstrings."""
    
    class WithoutType:  # pylint: disable=missing-class-docstring
        attr_one = "value"
        """Description for attr_one"""

    docstring = parse_from_object(WithoutType)

    assert docstring.short_description is None, f"Expected short description to be None, but got {docstring.short_description}"
    assert docstring.long_description is None, f"Expected long description to be None, but got {docstring.long_description}"
    assert docstring.description is None, f"Expected description to be None, but got {docstring.description}"
    assert len(docstring.params) == 1, f"Expected one parameter, but found {len(docstring.params)}"
    assert docstring.params[0].arg_name == "attr_one", f"Expected argument name to be 'attr_one', but got '{docstring.params[0].arg_name}'"
    assert docstring.params[0].type_name is None, f"Expected type name to be None, but got {docstring.params[0].type_name}"
    assert docstring.params[0].description == "Description for attr_one", f"Expected description to be 'Description for attr_one', but got '{docstring.params[0].description}'"
