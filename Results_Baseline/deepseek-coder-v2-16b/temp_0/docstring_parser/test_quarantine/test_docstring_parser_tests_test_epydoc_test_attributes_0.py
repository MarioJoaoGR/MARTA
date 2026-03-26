
# Module: docstring_parser.tests.test_epydoc
# Import the function using its provided module name.
from docstring_parser.tests.test_epydoc import parse as test_parse

def test_parse():
    # Test case for parsing an empty docstring
    docstring = test_parse("")
    assert len(docstring.params) == 0

    # Test case for parsing a short description without attributes
    docstring = test_parse("Short description")
    assert len(docstring.params) == 0

    # Test case for parsing multiple attributes in the epydoc style
    docstring = test_parse(
        """
        Short description

        @ivar name: description 1
        @ivar priority: description 2
        @type priority: int
        @cvar sender: description 3
        @type sender: str?
        @var message: description 4, defaults to 'hello'
        @type message: str?
        @var multiline: long description 5,
        defaults to 'bye'
        @type multiline: str?
        """
    )
    assert len(docstring.params) == 5
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].args[0] == "ivar"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1"
    assert docstring.params[0].default is None
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].args[0] == "ivar"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
    assert docstring.params[1].default is None
    assert docstring.params[2].arg_name == "sender"
    assert docstring.params[2].args[0] == "cvar"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description == "description 3"
    assert docstring.params[2].is_optional
    assert docstring.params[2].default is None
    assert docstring.params[3].arg_name == "message"
    assert docstring.params[3].args[0] == "var"
    assert docstring.params[3].type_name == "str"
    assert (
        docstring.params[3].description == "description 4, defaults to 'hello'"
    )
    assert docstring.params[3].is_optional
    assert docstring.params[3].default == "'hello'"
    assert docstring.params[4].arg_name == "multiline"
    assert docstring.params[4].type_name == "str"
    assert docstring.params[4].args[0] == "var"
    assert (
        docstring.params[4].description
        == "long description 5,\ndefaults to 'bye'"
    )
    assert docstring.params[4].is_optional
    assert docstring.params[4].default == "'bye'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_attributes_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_attributes_0.py:6:0: E0102: function already defined line 4 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_attributes_0.py:8:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_attributes_0.py:8:16: E1121: Too many positional arguments for function call (too-many-function-args)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_attributes_0.py:12:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_attributes_0.py:12:16: E1121: Too many positional arguments for function call (too-many-function-args)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_attributes_0.py:16:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_attributes_0.py:16:16: E1121: Too many positional arguments for function call (too-many-function-args)

"""