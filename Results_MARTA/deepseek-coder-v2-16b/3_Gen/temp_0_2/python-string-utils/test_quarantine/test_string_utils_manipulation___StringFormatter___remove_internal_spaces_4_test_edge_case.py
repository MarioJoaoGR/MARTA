
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_remove_internal_spaces():
    # Test with a simple string that has internal spaces
    formatter = __StringFormatter("Hello   World!")
    assert formatter._StringFormatter__remove_internal_spaces(re.match(r'(\S+)', "Hello   World!")) == "HelloWorld!"
    
    # Test with a string that already doesn't have internal spaces
    formatter = __StringFormatter("HelloWorld!")
    assert formatter._StringFormatter__remove_internal_spaces(re.match(r'(\S+)', "HelloWorld!")) == "HelloWorld!"
    
    # Test with a string that has leading and trailing spaces
    formatter = __StringFormatter("  Hello   World!  ")
    assert formatter._StringFormatter__remove_internal_spaces(re.match(r'(\S+)', "  Hello   World!  ")) == "HelloWorld!"
    
    # Test with an invalid input string, which should raise InvalidInputError
    try:
        __StringFormatter(12345)
        assert False, "Expected InvalidInputError but no error was raised"
    except InvalidInputError:
        assert True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_internal_spaces_4_test_edge_case
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_4_test_edge_case.py:8:11: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_internal_spaces' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_4_test_edge_case.py:12:11: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_internal_spaces' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_4_test_edge_case.py:16:11: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_internal_spaces' member (no-member)


"""