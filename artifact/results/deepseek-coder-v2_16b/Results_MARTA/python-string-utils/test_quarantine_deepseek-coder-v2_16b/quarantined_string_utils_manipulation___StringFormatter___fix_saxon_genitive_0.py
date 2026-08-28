
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

class TestStringFormatter:
    
    def test_valid_input(self):
        formatter = __StringFormatter("hello world")
        assert formatter.input_string == "hello world"
        
    def test_invalid_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
            __StringFormatter(12345)
        assert str(exc_info.value) == 'Expected "str", received "int"'
        
    def test_none_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
            __StringFormatter(None)
        assert str(exc_info.value) == 'Expected "str", received "NoneType"'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ TestStringFormatter.test_valid_input _____________________

self = <test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.TestStringFormatter object at 0x7f3c52843430>

    def test_valid_input(self):
>       formatter = __StringFormatter("hello world")
E       NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py:11: NameError
____________________ TestStringFormatter.test_invalid_input ____________________

self = <test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.TestStringFormatter object at 0x7f3c528432e0>

    def test_invalid_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringFormatter(12345)
E           NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py:16: NameError
_____________________ TestStringFormatter.test_none_input ______________________

self = <test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.TestStringFormatter object at 0x7f3c528435e0>

    def test_none_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringFormatter(None)
E           NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py:21: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py::TestStringFormatter::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py::TestStringFormatter::test_invalid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py::TestStringFormatter::test_none_input
============================== 3 failed in 0.06s ===============================
"""