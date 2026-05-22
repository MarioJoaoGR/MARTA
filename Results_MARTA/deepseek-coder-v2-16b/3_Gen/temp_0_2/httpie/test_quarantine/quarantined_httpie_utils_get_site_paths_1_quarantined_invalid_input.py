
import pytest
from unittest.mock import patch
from pathlib import Path
from httpie.utils import get_site_paths, MIN_SUPPORTED_PY_VERSION, MAX_SUPPORTED_PY_VERSION

def test_invalid_input():
    with pytest.raises(TypeError):
        with patch('httpie.compat.is_frozen', return_value=False):
            list(get_site_paths(Path('/invalid/path')))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_get_site_paths_1_test_invalid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_site_paths_1_test_invalid_input.py:5:0: E0611: No name 'MIN_SUPPORTED_PY_VERSION' in module 'httpie.utils' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_site_paths_1_test_invalid_input.py:5:0: E0611: No name 'MAX_SUPPORTED_PY_VERSION' in module 'httpie.utils' (no-name-in-module)


"""