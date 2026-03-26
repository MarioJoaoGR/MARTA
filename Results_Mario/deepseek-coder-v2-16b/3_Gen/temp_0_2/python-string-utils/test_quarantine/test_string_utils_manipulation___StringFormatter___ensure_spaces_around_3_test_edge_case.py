
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_edge_case():
    formatter = __StringFormatter("HelloWorld")
    match = re.match(r'(He)(ll)(o)', formatter.input_string)
    
    assert formatter._StringFormatter__ensure_spaces_around(match) == ' Hello World '

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_spaces_around_3_test_edge_case
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_3_test_edge_case.py:9:11: E1101: Instance of '__StringFormatter' has no '_StringFormatter__ensure_spaces_around' member (no-member)


"""