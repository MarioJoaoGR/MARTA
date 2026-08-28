
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

class Test__StringFormatter:
    
    def test_valid_initialization(self):
        formatter = __StringFormatter("This is a valid string.")
        assert formatter.input_string == "This is a valid string."
        
    def test_invalid_initialization(self):
        with pytest.raises(InvalidInputError) as excinfo:
            __StringFormatter(12345)
        assert str(excinfo.value) == 'Expected "str", received "int"'
        
    @pytest.mark.parametrize("input_string, expected", [
        ("Hello   World", "Hello World"),
        ("  This is a test  ", "This is a test"),
        ("", "")
    ])
    def test_format_string_valid(self, input_string, expected):
        formatted_string = __StringFormatter.format_string(input_string)
        assert formatted_string == expected
        
    @pytest.mark.parametrize("input_string", [
        "This is a test email address: example@example.com and a test URL: http://www.example.com."
    ])
    def test_format_string_invalid(self, input_string):
        with pytest.raises(InvalidInputError) as excinfo:
            __StringFormatter(input_string)
        assert str(excinfo.value) == 'Expected "str", received "str"'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 6 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
_______________ Test__StringFormatter.test_valid_initialization ________________

self = <test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.Test__StringFormatter object at 0x7fc6b68de2f0>

    def test_valid_initialization(self):
>       formatter = __StringFormatter("This is a valid string.")
E       NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py:11: NameError
______________ Test__StringFormatter.test_invalid_initialization _______________

self = <test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.Test__StringFormatter object at 0x7fc6b68dd510>

    def test_invalid_initialization(self):
        with pytest.raises(InvalidInputError) as excinfo:
>           __StringFormatter(12345)
E           NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py:16: NameError
__ Test__StringFormatter.test_format_string_valid[Hello   World-Hello World] ___

self = <test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.Test__StringFormatter object at 0x7fc6b68deb30>
input_string = 'Hello   World', expected = 'Hello World'

    @pytest.mark.parametrize("input_string, expected", [
        ("Hello   World", "Hello World"),
        ("  This is a test  ", "This is a test"),
        ("", "")
    ])
    def test_format_string_valid(self, input_string, expected):
>       formatted_string = __StringFormatter.format_string(input_string)
E       NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py:25: NameError
_ Test__StringFormatter.test_format_string_valid[  This is a test  -This is a test] _

self = <test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.Test__StringFormatter object at 0x7fc6b68dd660>
input_string = '  This is a test  ', expected = 'This is a test'

    @pytest.mark.parametrize("input_string, expected", [
        ("Hello   World", "Hello World"),
        ("  This is a test  ", "This is a test"),
        ("", "")
    ])
    def test_format_string_valid(self, input_string, expected):
>       formatted_string = __StringFormatter.format_string(input_string)
E       NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py:25: NameError
______________ Test__StringFormatter.test_format_string_valid[-] _______________

self = <test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.Test__StringFormatter object at 0x7fc6b68de440>
input_string = '', expected = ''

    @pytest.mark.parametrize("input_string, expected", [
        ("Hello   World", "Hello World"),
        ("  This is a test  ", "This is a test"),
        ("", "")
    ])
    def test_format_string_valid(self, input_string, expected):
>       formatted_string = __StringFormatter.format_string(input_string)
E       NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py:25: NameError
_ Test__StringFormatter.test_format_string_invalid[This is a test email address: example@example.com and a test URL: http://www.example.com.] _

self = <test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.Test__StringFormatter object at 0x7fc6b68dee00>
input_string = 'This is a test email address: example@example.com and a test URL: http://www.example.com.'

    @pytest.mark.parametrize("input_string", [
        "This is a test email address: example@example.com and a test URL: http://www.example.com."
    ])
    def test_format_string_invalid(self, input_string):
        with pytest.raises(InvalidInputError) as excinfo:
>           __StringFormatter(input_string)
E           NameError: name '_Test__StringFormatter__StringFormatter' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py:33: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py::Test__StringFormatter::test_valid_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py::Test__StringFormatter::test_invalid_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py::Test__StringFormatter::test_format_string_valid[Hello   World-Hello World]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py::Test__StringFormatter::test_format_string_valid[  This is a test  -This is a test]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py::Test__StringFormatter::test_format_string_valid[-]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_1.py::Test__StringFormatter::test_format_string_invalid[This is a test email address: example@example.com and a test URL: http:/www.example.com.]
============================== 6 failed in 0.08s ===============================
"""