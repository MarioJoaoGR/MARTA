
from docstring_parser import parse as dp_parse
from docstring_parser.common import Param

class MockParse:
    def __init__(self):
        self.return_value = None

    def return_value(self, value):
        self.return_value = value
        return self.return_value

def test_params():
    """Test parsing parameters from a docstring."""
    mock_parse = MockParse()
    
    # Test without any parameters
    docstring = dp_parse("")
    assert len(docstring.params) == 0

    # Example with multiple parameters
    rest_doc = """
    Short description

    :param name: description 1
    :param int priority: description 2
    :param str? sender: description 3
    :param str? message: description 4, defaults to 'hello'
    :param str? multiline: long description 5, defaults to 'bye'
    """
    mock_parse.return_value = dp_parse(rest_doc)
    docstring = mock_parse.return_value()
    
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

    # Additional test with different parameters
    docstring = dp_parse(
        """
        Short description

        :param a: description a
        :type a: int
        :param int b: description b
        """
    )
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "a"
    assert docstring.params[0].type_name == "int"
    assert docstring.params[0].description == "description a"
    assert docstring.params[0].default is None
    assert not docstring.params[0].is_optional
    
    assert docstring.params[1].arg_name == "b"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description b"
    assert not docstring.params[1].is_optional

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_params_0_test_test_params_basic
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_0_test_test_params_basic.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_0_test_test_params_basic.py:3:0: E0611: No name 'Param' in module 'docstring_parser.common' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_0_test_test_params_basic.py:9:4: E0202: An attribute defined in Test4DT_tests.test_docstring_parser_tests_test_rest_test_params_0_test_test_params_basic line 7 hides this method (method-hidden)


"""