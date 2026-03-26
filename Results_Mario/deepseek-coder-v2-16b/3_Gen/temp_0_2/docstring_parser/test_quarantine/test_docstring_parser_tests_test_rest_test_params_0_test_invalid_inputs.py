
import pytest
from docstring_parser import parse as dp_parse
from docstring_parser.models import Docstring, Param

class MockParse:
    def __init__(self):
        self.params = []
    
    def return_value(self, value):
        if isinstance(value, Docstring):
            self.params = [param for param in value.params]
        return self

@pytest.fixture
def mock_parse():
    return MockParse()

def test_params(mock_parse):
    """Test parsing parameters from a docstring."""
    # Test without any parameters
    docstring = dp_parse("Short description")
    assert len(docstring.params) == 0

    # Test with multiple parameters
    mock_parse.return_value = Docstring(params=[Param(name="name", type_name=None, description="description 1", default=None), Param(name="priority", type_name="int", description="description 2", default=None), Param(name="sender", type_name="str", description="description 3", default=None), Param(name="message", type_name="str", description="description 4, defaults to 'hello'", default=None), Param(name="multiline", type_name="str", description="long description 5, defaults to 'bye'", default=None)])
    docstring = mock_parse.return_value("Short description")
    assert len(docstring.params) == 5
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1"
    assert docstring.params[0].default is None
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
    assert docstring.params[1].default is None
    assert docstring.params[2].arg_name == "sender"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description == "description 3"
    assert docstring.params[2].is_optional
    assert docstring.params[2].default is None
    assert docstring.params[3].arg_name == "message"
    assert docstring.params[3].type_name == "str"
    assert docstring.params[3].description == "description 4, defaults to 'hello'"
    assert docstring.params[3].is_optional
    assert docstring.params[3].default == "'hello'"
    assert docstring.params[4].arg_name == "multiline"
    assert docstring.params[4].type_name == "str"
    assert docstring.params[4].description == "long description 5, defaults to 'bye'"
    assert docstring.params[4].is_optional
    assert docstring.params[4].default == "'bye'"

    # Test with required and optional parameters mixed
    docstring = dp_parse(
        """
        Short description

        :param a: description a
        :type a: int
        :param b: description b
        :type b: int
        """
    )
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "a"
    assert docstring.params[0].type_name == "int"
    assert docstring.params[0].description == "description a"
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "b"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description b"
    assert not docstring.params[1].is_optional

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_params_0_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_0_test_invalid_inputs.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_0_test_invalid_inputs.py:4:0: E0401: Unable to import 'docstring_parser.models' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_0_test_invalid_inputs.py:4:0: E0611: No name 'models' in module 'docstring_parser' (no-name-in-module)


"""