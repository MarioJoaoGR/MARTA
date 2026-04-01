
import re
from string_utils.manipulation import asciify

def test_valid_input():
    # Test case 1: Converting a typical title to slug
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    
    # Test case 2: Handling non-ASCII characters by converting them to their closest ASCII equivalents
    assert slugify('Mönstér Mägnët') == 'monster-magnet'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_slugify_3_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_3_test_valid_input.py:7:11: E0602: Undefined variable 'slugify' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_3_test_valid_input.py:10:11: E0602: Undefined variable 'slugify' (undefined-variable)


"""