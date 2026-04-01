
from docstring_parser.tests.test_numpydoc import parse

def test_other_params() -> None:
    """Test parsing other parameters in a numpy-style docstring.

    This function is designed to test the parsing of additional or less commonly used parameters within a numpy-style docstring. It takes an optional string `text` which represents a numpy-style docstring and parses it using the NumpydocParser class. The purpose of this testing function is to ensure that specific sections for such parameters are correctly identified, their types and descriptions are accurately parsed, and whether they are optional or not is verified.

    Parameters:
        text (Optional[str]): A string containing a numpy-style docstring. This parameter is optional as the function can also accept None, in which case it will return an empty or default parsed result based on the parser's configuration.
            - If provided, changes to this input string can affect what sections are recognized and how they are formatted during parsing.
            - If not provided (or set to None), the function will use a default configuration for parsing which may include standard sections like "Parameters" and "Returns".

    Returns:
        None: This function does not return any value but rather performs assertions on the parsed docstring metadata to ensure correctness in parameter handling.

    Examples:
        >>> # Example usage of test_other_params() would typically involve checking for specific outcomes based on expected configurations or inputs, as this is a testing function and its main purpose is validation.
    """
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
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == [
        "other_param",
        "only_seldom_used_keywords",
    ]
    assert docstring.meta[0].arg_name == "only_seldom_used_keywords"
    assert docstring.meta[0].type_name == "type"
    assert docstring.meta[0].is_optional
    assert docstring.meta[0].description == "Explanation"

    assert docstring.meta[1].args == [
        "other_param",
        "common_parameters_listed_above",
    ]
    assert docstring.meta[1].arg_name == "common_parameters_listed_above"
    assert docstring.meta[1].type_name == "type"
    assert docstring.meta[1].is_optional
    assert docstring.meta[1].description == "Explanation"
