
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

class Test__StringFormatter:
    
    def test_valid_input_string(self):
        formatter = __StringFormatter("hello world")
        assert is_string(formatter.input_string)
        assert formatter.input_string == "hello world"
    
    def test_invalid_input_type(self):
        with pytest.raises(InvalidInputError) as excinfo:
            __StringFormatter(12345)
        assert str(excinfo.value) == 'Expected "str", received "int"'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________ Test__StringFormatter.test_valid_input_string _________________

self = <test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.Test__StringFormatter object at 0x7f6de597f5e0>

    def test_valid_input_string(self):
>       formatter = __StringFormatter("hello world")
E       NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.py:11: NameError
________________ Test__StringFormatter.test_invalid_input_type _________________

self = <test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.Test__StringFormatter object at 0x7f6de597f880>

    def test_invalid_input_type(self):
        with pytest.raises(InvalidInputError) as excinfo:
>           __StringFormatter(12345)
E           NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.py:17: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.py::Test__StringFormatter::test_valid_input_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.py::Test__StringFormatter::test_invalid_input_type
============================== 2 failed in 0.06s ===============================
"""