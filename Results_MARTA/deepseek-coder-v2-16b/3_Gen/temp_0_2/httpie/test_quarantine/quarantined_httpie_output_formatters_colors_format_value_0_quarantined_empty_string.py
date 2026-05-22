
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_color

def format_value(value):
    return ' '.join(get_color(part, shade) or part for part in value.split())

@pytest.mark.parametrize("input_value, expected", [("", "")])
def test_empty_string(input_value, expected):
    with patch('httpie.output.formatters.colors.get_color') as mock_get_color:
        # Mock the return value of get_color to always return None for all parts
        mock_get_color.return_value = None
        
        assert format_value(input_value) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_format_value_0_test_empty_string
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_format_value_0_test_empty_string.py:7:36: E0602: Undefined variable 'shade' (undefined-variable)


"""