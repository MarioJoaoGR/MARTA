
import re
from string_utils.validation import is_snake_case, SNAKE_CASE_TEST_RE, SNAKE_CASE_TEST_DASH_RE
from unittest.mock import patch

def test_valid_case():
    # Test a valid snake case string
    with patch('string_utils.validation.SNAKE_CASE_TEST_RE', new=re.compile(r'^[a-z]+(_[a-z]+)*$')):
        with patch('string_utils.validation.SNAKE_CASE_TEST_DASH_RE', new=re.compile(r'^[a-z]+(-[a-z]+)*$')):
            assert is_snake_case('foo_bar_baz') == True
            assert is_snake_case('foo_123_bar') == False  # Updated to check for invalid case
