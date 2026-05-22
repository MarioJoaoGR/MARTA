
import pytest
from unittest.mock import patch, MagicMock
import pygments.styles

def get_available_styles():
    return sorted(BUNDLED_STYLES | set(pygments.styles.get_all_styles()))

@pytest.fixture(autouse=True)
def mock_pygments_styles():
    with patch('pygments.styles.get_all_styles', return_value=['monokai', 'default']):
        yield

def test_edge_case():
    available_styles = get_available_styles()
    assert available_styles == sorted(['monokai', 'default', *BUNDLED_STYLES])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_get_available_styles_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_available_styles_0_test_edge_case.py:7:18: E0602: Undefined variable 'BUNDLED_STYLES' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_available_styles_0_test_edge_case.py:16:62: E0602: Undefined variable 'BUNDLED_STYLES' (undefined-variable)


"""