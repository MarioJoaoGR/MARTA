
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.manipulation import InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

class TestStringFormatter:
    
    def test_valid_initialization(self):
        formatter = __StringFormatter("valid_input")
        assert formatter.input_string == "valid_input"
        
    def test_invalid_initialization(self):
        with pytest.raises(InvalidInputError) as excinfo:
            __StringFormatter(12345)
        assert str(excinfo.value) == "Expected 'str', received 'int'"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________ TestStringFormatter.test_valid_initialization _________________

self = <test_string_utils_manipulation___StringFormatter___ensure_spaces_around_1.TestStringFormatter object at 0x7f436503a7a0>

    def test_valid_initialization(self):
>       formatter = __StringFormatter("valid_input")
E       NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_1.py:12: NameError
_______________ TestStringFormatter.test_invalid_initialization ________________

self = <test_string_utils_manipulation___StringFormatter___ensure_spaces_around_1.TestStringFormatter object at 0x7f4365039f00>

    def test_invalid_initialization(self):
        with pytest.raises(InvalidInputError) as excinfo:
>           __StringFormatter(12345)
E           NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_1.py:17: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_1.py::TestStringFormatter::test_valid_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_1.py::TestStringFormatter::test_invalid_initialization
============================== 2 failed in 0.06s ===============================
"""