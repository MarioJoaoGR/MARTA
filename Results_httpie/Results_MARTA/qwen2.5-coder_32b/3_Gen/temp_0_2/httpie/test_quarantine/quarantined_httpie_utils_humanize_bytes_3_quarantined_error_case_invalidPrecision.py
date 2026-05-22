
import pytest
from humanize_bytes import humanize_bytes

def test_error_case_invalidPrecision():
    with pytest.raises(ValueError):
        humanize_bytes(1024, precision=-1)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_utils_humanize_bytes_3_test_error_case_invalidPrecision
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_humanize_bytes_3_test_error_case_invalidPrecision.py:3:0: E0401: Unable to import 'humanize_bytes' (import-error)


"""