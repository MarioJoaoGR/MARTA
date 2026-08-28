
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

class TestStringFormatter:
    
    def test_valid_input(self):
        input_string = "This is a valid input string."
        formatter = __StringFormatter(input_string)
        assert isinstance(formatter, __StringFormatter), "Expected formatter to be an instance of __StringFormatter"
        formatted_string = formatter.format()
        assert formatted_string == "This is a valid input string.", f"Expected '{formatted_string}' to be 'This is a valid input string.'"
    
    def test_invalid_input(self):
        input_string = None
        with pytest.raises(InvalidInputError) as excinfo:
            formatter = __StringFormatter(input_string)
        assert isinstance(excinfo.value, InvalidInputError), "Expected an InvalidInputError to be raised"
    
    def test_empty_input(self):
        input_string = ""
        with pytest.raises(InvalidInputError) as excinfo:
            formatter = __StringFormatter(input_string)
        assert isinstance(excinfo.value, InvalidInputError), "Expected an InvalidInputError to be raised"
    
    def test_whitespace_only_input(self):
        input_string = "   "
        with pytest.raises(InvalidInputError) as excinfo:
            formatter = __StringFormatter(input_string)
        assert isinstance(excinfo.value, InvalidInputError), "Expected an InvalidInputError to be raised"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________________ TestStringFormatter.test_valid_input _____________________

self = <test_string_utils_manipulation_prettify_2.TestStringFormatter object at 0x7fa98c6d6110>

    def test_valid_input(self):
        input_string = "This is a valid input string."
>       formatter = __StringFormatter(input_string)
E       NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py:9: NameError
____________________ TestStringFormatter.test_invalid_input ____________________

self = <test_string_utils_manipulation_prettify_2.TestStringFormatter object at 0x7fa98c6d55d0>

    def test_invalid_input(self):
        input_string = None
        with pytest.raises(InvalidInputError) as excinfo:
>           formatter = __StringFormatter(input_string)
E           NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py:17: NameError
_____________________ TestStringFormatter.test_empty_input _____________________

self = <test_string_utils_manipulation_prettify_2.TestStringFormatter object at 0x7fa98c6d5d50>

    def test_empty_input(self):
        input_string = ""
        with pytest.raises(InvalidInputError) as excinfo:
>           formatter = __StringFormatter(input_string)
E           NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py:23: NameError
________________ TestStringFormatter.test_whitespace_only_input ________________

self = <test_string_utils_manipulation_prettify_2.TestStringFormatter object at 0x7fa98c6d6500>

    def test_whitespace_only_input(self):
        input_string = "   "
        with pytest.raises(InvalidInputError) as excinfo:
>           formatter = __StringFormatter(input_string)
E           NameError: name '_TestStringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py:29: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py::TestStringFormatter::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py::TestStringFormatter::test_invalid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py::TestStringFormatter::test_empty_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_prettify_2.py::TestStringFormatter::test_whitespace_only_input
============================== 4 failed in 0.07s ===============================
"""