
import pytest
from unittest.mock import MagicMock, patch
from httpie.uploads import _wrap_function_with_callback

def test_invalid_callback():
    with patch('httpie.uploads._wrap_function_with_callback') as mock_wrap:
        # Mock the function and callback
        func = MagicMock()
        callback = "not a callable"

        # Call the wrapped function
        with pytest.raises(TypeError):
            _wrap_function_with_callback(func, callback)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads__wrap_function_with_callback_1_test_invalid_callback.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_callback _____________________________

    def test_invalid_callback():
        with patch('httpie.uploads._wrap_function_with_callback') as mock_wrap:
            # Mock the function and callback
            func = MagicMock()
            callback = "not a callable"
    
            # Call the wrapped function
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads__wrap_function_with_callback_1_test_invalid_callback.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads__wrap_function_with_callback_1_test_invalid_callback.py::test_invalid_callback
============================== 1 failed in 0.16s ===============================
"""