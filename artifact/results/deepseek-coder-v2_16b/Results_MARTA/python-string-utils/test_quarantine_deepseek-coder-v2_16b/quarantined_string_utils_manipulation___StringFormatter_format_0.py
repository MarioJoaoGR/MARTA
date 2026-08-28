
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

class Test__StringFormatter:
    
    def test_none_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
            __StringFormatter(None)
        assert str(exc_info.value) == 'Expected "str", received "NoneType"'

    def test_invalid_type_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
            __StringFormatter(12345)
        assert str(exc_info.value) == 'Expected "str", received "int"'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter_format_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________ Test__StringFormatter.test_none_input _____________________

self = <test_string_utils_manipulation___StringFormatter_format_0.Test__StringFormatter object at 0x7fe1d06e2ad0>

    def test_none_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringFormatter(None)
E           NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter_format_0.py:14: NameError
________________ Test__StringFormatter.test_invalid_type_input _________________

self = <test_string_utils_manipulation___StringFormatter_format_0.Test__StringFormatter object at 0x7fe1d06e24a0>

    def test_invalid_type_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringFormatter(12345)
E           NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter_format_0.py:19: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter_format_0.py::Test__StringFormatter::test_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter_format_0.py::Test__StringFormatter::test_invalid_type_input
============================== 2 failed in 0.07s ===============================
"""