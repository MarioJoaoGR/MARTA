
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        formatter = __StringFormatter('hello world')
        match = re.match(r'\w+', 'hello')
        result = formatter._StringFormatter__uppercase_first_char(match)
>       assert result == 'Hello'
E       AssertionError: assert 'HELLO' == 'Hello'
E         
E         - Hello
E         + HELLO

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:9: AssertionError
________________________ test_invalid_input_non_string _________________________

    def test_invalid_input_non_string():
>       with pytest.raises(InvalidInputError):
E       NameError: name 'pytest' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:12: NameError
___________________ test_uppercase_first_char_with_no_match ____________________

    def test_uppercase_first_char_with_no_match():
        formatter = __StringFormatter('hello world')
        match = re.match(r'\d+', 'hello')  # No match
>       assert formatter._StringFormatter__uppercase_first_char(match) is None

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.manipulation.__StringFormatter object at 0x7f55076d7b20>
regex_match = None

    def __uppercase_first_char(self, regex_match):
>       return regex_match.group(0).upper()
E       AttributeError: 'NoneType' object has no attribute 'group'

/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/manipulation.py:220: AttributeError
_______________ test_uppercase_first_char_with_full_string_match _______________

    def test_uppercase_first_char_with_full_string_match():
        formatter = __StringFormatter('hello')
        match = re.match(r'\w+', 'hello')
        result = formatter._StringFormatter__uppercase_first_char(match)
>       assert result == 'Hello'
E       AssertionError: assert 'HELLO' == 'Hello'
E         
E         - Hello
E         + HELLO

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:24: AssertionError
_____________ test_uppercase_first_char_with_partial_string_match ______________

    def test_uppercase_first_char_with_partial_string_match():
        formatter = __StringFormatter('hello world')
        match = re.match(r'\w+', 'hello world')  # Matches 'hello'
        result = formatter._StringFormatter__uppercase_first_char(match)
>       assert result == 'Hello'
E       AssertionError: assert 'HELLO' == 'Hello'
E         
E         - Hello
E         + HELLO

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:30: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py::test_invalid_input_non_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py::test_uppercase_first_char_with_no_match
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py::test_uppercase_first_char_with_full_string_match
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py::test_uppercase_first_char_with_partial_string_match
============================== 5 failed in 0.08s ===============================
"""