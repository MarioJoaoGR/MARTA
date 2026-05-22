
import pytest
from unittest.mock import patch
from httpie.models import HTTPRequest

def test_invalid_input():
    with pytest.raises(TypeError):
        request = HTTPRequest()
        list(request.iter_lines("not an integer"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_models_HTTPRequest_iter_lines_0_test_invalid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPRequest_iter_lines_0_test_invalid_input.py:8:18: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""