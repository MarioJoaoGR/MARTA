
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.mark.parametrize("rest_doc, expected_type, expected_description", [
    (":returns: description", None, "description"),
    (":returns int:", "int", ""),
    (":returns: description\n:rtype: int", "int", "description")
])
def test_valid_input_with_return_description(rest_doc, expected_type, expected_description):
    docstring = parse(rest_doc)
    assert docstring.returns is not None
    if expected_type is not None:
        assert docstring.returns.type_name == expected_type
    else:
        assert docstring.returns.type_name is None
    assert docstring.returns.description == expected_description
    assert not docstring.returns.is_generator
