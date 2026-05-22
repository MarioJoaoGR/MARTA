
import pytest
from unittest.mock import patch, MagicMock
import pygments.styles

def get_available_styles():
    return sorted(BUNDLED_STYLES | set(pygments.styles.get_all_styles()))

@pytest.mark.parametrize("exception_to_raise", [ValueError])
def test_error_case(exception_to_raise):
    with patch('pygments.styles.get_all_styles', side_effect=exception_to_raise):
        with pytest.raises(ValueError):
            get_available_styles()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_get_available_styles_2_test_error_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_available_styles_2_test_error_case.py:7:18: E0602: Undefined variable 'BUNDLED_STYLES' (undefined-variable)


"""