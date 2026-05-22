
from httpie.output.formatters.colors import BUNDLED_STYLES, get_all_styles
import pytest
from unittest.mock import patch

def get_available_styles():
    return sorted(BUNDLED_STYLES | set(get_all_styles()))

def test_get_available_styles():
    with patch('httpie.output.formatters.colors.get_all_styles') as mock_get_all_styles:
        # Mock the return value of get_all_styles to simulate available styles
        mock_get_all_styles.return_value = ['monokai', 'default']

        # Call the function under test
        available_styles = get_available_styles()

        # Assert that the function returns a sorted list of available styles
        assert isinstance(available_styles, list)
        assert set(available_styles) == BUNDLED_STYLES | {'monokai', 'default'}
        assert available_styles == ['default', 'monokai']  # Sorted order

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_get_available_styles_0_test_valid_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_available_styles_0_test_valid_case.py:2:0: E0611: No name 'get_all_styles' in module 'httpie.output.formatters.colors' (no-name-in-module)


"""