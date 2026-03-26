
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse

def test_other_params() -> None:
    """Test parsing other parameters."""
    # Test case for line 483, where the function parses a docstring with other parameters
    docstring = parse(
        """
        Short description
        Other Parameters
        ----------------
        only_seldom_used_keywords : type, optional
            Explanation
        common_parameters_listed_above : type, optional
            Explanation
        """
    )
    
    # Test case for line 494, checking the length of meta attribute
    assert len(docstring.meta) == 2
    
    # Test case for line 495, checking the first parameter's args
    assert docstring.meta[0].args == ["other_param", "only_seldom_used_keywords"]
    
    # Test case for lines 499-502, checking details of the first parameter
    assert docstring.meta[0].arg_name == "only_seldom_used_keywords"
    assert docstring.meta[0].type_name == "type"
    assert docstring.meta[0].is_optional is True
    assert docstring.meta[0].description == "Explanation"
    
    # Test case for line 504, checking the second parameter's args
    assert docstring.meta[1].args == ["other_param", "common_parameters_listed_above"]
