
import pytest
from docstring_parser import parse

def test_yields() -> None:
    """Test parsing yields."""
    with pytest.raises(Exception):
        docstring = parse("Short description")
    
    with pytest.raises(Exception):
        docstring = parse("""Short description :yields: description""")
    
    docstring = parse("""Short description :yields int: description""")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_yields_0_test_invalid_input_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_yields_0_test_invalid_input_error_handling.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""