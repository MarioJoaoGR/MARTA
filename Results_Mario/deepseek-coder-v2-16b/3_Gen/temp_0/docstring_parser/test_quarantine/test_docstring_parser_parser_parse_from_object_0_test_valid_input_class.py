
import pytest
from docstring_parser import DocstringStyle, parse_from_object
from unittest.mock import patch

@pytest.mark.parametrize("obj", [MyClass])
def test_valid_input_class(obj):
    with patch('docstring_parser.parser.parse') as mock_parse:
        mock_parse.return_value = Docstring()
        
        parsed_obj = parse_from_object(obj)
        
        assert isinstance(parsed_obj, Docstring)
        mock_parse.assert_called_once_with(obj.__doc__, style=DocstringStyle.AUTO)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_parser_parse_from_object_0_test_valid_input_class
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_valid_input_class.py:3:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_valid_input_class.py:3:0: E0611: No name 'parse_from_object' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_valid_input_class.py:6:33: E0602: Undefined variable 'MyClass' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_valid_input_class.py:9:34: E0602: Undefined variable 'Docstring' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_valid_input_class.py:13:38: E0602: Undefined variable 'Docstring' (undefined-variable)


"""