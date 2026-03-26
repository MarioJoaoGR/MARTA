
import pytest
from string_utils.manipulation import compress

@pytest.mark.parametrize("input_string", ["Hello, World!"])
def test_valid_input(input_string):
    compressed = compress(input_string)
    assert len(compressed) < len(input_string), "Compressed string should be shorter than the original"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_compress_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input[Hello, World!] ________________________

input_string = 'Hello, World!'

    @pytest.mark.parametrize("input_string", ["Hello, World!"])
    def test_valid_input(input_string):
        compressed = compress(input_string)
>       assert len(compressed) < len(input_string), "Compressed string should be shorter than the original"
E       AssertionError: Compressed string should be shorter than the original
E       assert 28 < 13
E        +  where 28 = len('eNrzSM3JyddRCM8vyklRBAAfngRq')
E        +  and   13 = len('Hello, World!')

python-string-utils/Test4DT_tests/test_string_utils_manipulation_compress_0_test_valid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_compress_0_test_valid_input.py::test_valid_input[Hello, World!]
============================== 1 failed in 0.02s ===============================
"""