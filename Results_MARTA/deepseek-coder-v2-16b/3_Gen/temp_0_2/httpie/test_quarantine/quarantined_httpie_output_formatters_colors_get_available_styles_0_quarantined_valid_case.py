
import pytest
from unittest.mock import patch, MagicMock
import pygments.styles

def get_available_styles():
    return sorted(BUNDLED_STYLES | set(pygments.styles.get_all_styles()))

@pytest.fixture(autouse=True)
def mock_pygments_styles():
    with patch('pygments.styles.get_all_styles', return_value=['style1', 'style2']):
        yield

def test_valid_case():
    available_styles = get_available_styles()
    assert sorted(['style1', 'style2']) == available_styles

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_get_available_styles_0_test_valid_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_available_styles_0_test_valid_case.py:7:18: E0602: Undefined variable 'BUNDLED_STYLES' (undefined-variable)


"""