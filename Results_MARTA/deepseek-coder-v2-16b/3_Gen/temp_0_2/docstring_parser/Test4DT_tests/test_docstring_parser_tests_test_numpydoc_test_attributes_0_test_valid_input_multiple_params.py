
from docstring_parser.tests.test_numpydoc import parse

def test_valid_input_multiple_params():
    """Test parsing attributes from a numpy-style docstring."""
    
    # Example with multiple parameters specified
    parsed_doc = parse(
        """
        Short description
        Attributes
        ----------
        name
            description 1
        priority : int
            description 2
        sender : str, optional
            description 3
        ratio : Optional[float], optional
            description 4
        """
    )
    assert len(parsed_doc.params) == 4
    assert parsed_doc.params[0].arg_name == "name"
    assert parsed_doc.params[0].type_name is None
    assert parsed_doc.params[0].description == "description 1"
    assert not parsed_doc.params[0].is_optional
    assert parsed_doc.params[1].arg_name == "priority"
    assert parsed_doc.params[1].type_name == "int"
    assert parsed_doc.params[1].description == "description 2"
    assert not parsed_doc.params[1].is_optional
    assert parsed_doc.params[2].arg_name == "sender"
    assert parsed_doc.params[2].type_name == "str"
    assert parsed_doc.params[2].description == "description 3"
    assert parsed_doc.params[2].is_optional
    assert parsed_doc.params[3].arg_name == "ratio"
    assert parsed_doc.params[3].type_name == "Optional[float]"
    assert parsed_doc.params[3].description == "description 4"
    assert parsed_doc.params[3].is_optional
    
    # Example with incomplete or no parameters specified
    incomplete_parsed_doc = parse(
        """
        Short description
        Attributes
        ----------
        name
            description 1
            with multi-line text
        priority : int
            description 2
        """
    )
    assert len(incomplete_parsed_doc.params) == 2
    assert incomplete_parsed_doc.params[0].arg_name == "name"
    assert incomplete_parsed_doc.params[0].type_name is None
    assert incomplete_parsed_doc.params[0].description == (
        "description 1\nwith multi-line text"
    )
    assert incomplete_parsed_doc.params[1].arg_name == "priority"
    assert incomplete_parsed_doc.params[1].type_name == "int"
    assert incomplete_parsed_doc.params[1].description == "description 2"
