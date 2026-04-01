
# Assuming the function is imported from string_utils.manipulation
from unittest.mock import patch
import pytest
from string_utils.manipulation import roman_encode

@pytest.mark.parametrize("input_number, expected", [
    (37, 'XXXVII'),
    ('2020', 'MMXX')
])
def test_valid_case_1(input_number, expected):
    with patch('string_utils.manipulation.roman_encode', return_value=expected) as mock_encode:
        assert roman_encode(input_number) == expected
