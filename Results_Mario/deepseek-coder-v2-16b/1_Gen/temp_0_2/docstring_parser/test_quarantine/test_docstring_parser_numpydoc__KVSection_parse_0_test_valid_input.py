
import pytest
from docstring_parser.numpydoc import _KVSection

def test_valid_input():
    """Test case for validating the parse method with valid input."""
    parser = _KVSection()
    docstring_text = """
    Summary line.
    
    Extended description of what the function does.
    
    Parameters:
        param1 (type): Description of parameter 1.
        param2 (:obj:`anotherType`): Description of parameter 2.
        
    Returns:
        return_type: Description of the return type.
    """
    parsed_items = list(parser.parse(docstring_text))
    
    assert len(parsed_items) == 3, "Expected three items to be parsed."
    
    # Check each item's key and value
    meta1, meta2, meta3 = parsed_items
    assert meta1.key == 'param1', f"Expected key 'param1', but got {meta1.key}"
    assert meta1.value == 'Description of parameter 1.', f"Expected value 'Description of parameter 1.', but got {meta1.value}"
    assert meta2.key == 'param2', f"Expected key 'param2', but got {meta2.key}"
    assert meta2.value == 'Description of parameter 2.', f"Expected value 'Description of parameter 2.', but got {meta2.value}"
    assert meta3.key == 'Returns', f"Expected key 'Returns', but got {meta3.key}"
    assert meta3.value == 'Description of the return type.', f"Expected value 'Description of the return type.', but got {meta3.value}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc__KVSection_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test_valid_input.py:7:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test_valid_input.py:7:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""