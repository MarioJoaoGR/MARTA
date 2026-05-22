
import pytest
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_init_with_none(self):
        with pytest.raises(TypeError):
            HTTPMessage()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_models_HTTPMessage___init___0_test_none_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage___init___0_test_none_input.py:8:12: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""