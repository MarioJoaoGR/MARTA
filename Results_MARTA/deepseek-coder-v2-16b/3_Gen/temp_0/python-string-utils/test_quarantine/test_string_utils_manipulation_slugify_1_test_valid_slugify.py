
import re
from your_module import slugify

def test_valid_slugify():
    # Test case 1: Basic title conversion
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    
    # Test case 2: Handling non-ASCII characters
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    
    # Additional test cases can be added here to cover different scenarios

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_slugify_1_test_valid_slugify
python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_1_test_valid_slugify.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""