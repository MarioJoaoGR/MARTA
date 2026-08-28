
import pytest
from string_utils.manipulation import __StringFormatter







"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 7 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py F [ 14%]
FFFFFF                                                                   [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        formatter = __StringFormatter("hello,world!this.is.a.test.")
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.'
E       AssertionError: assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py:8: AssertionError
_________________________ test_punctuation_and_spacing _________________________

    def test_punctuation_and_spacing():
        formatter = __StringFormatter("hello,world!this.is.a.test.")
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.'
E       AssertionError: assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py:13: AssertionError
__________________________ test_uppercase_after_sign ___________________________

    def test_uppercase_after_sign():
        formatter = __StringFormatter("hello:world!this.is.a.test.")
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello: World! This is a test.'
E       AssertionError: assert 'Hello: world... Is. A. Test.' == 'Hello: World...is is a test.'
E         
E         - Hello: World! This is a test.
E         + Hello: world! This. Is. A. Test.

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py:18: AssertionError
____________________________ test_remove_duplicates ____________________________

    def test_remove_duplicates():
        formatter = __StringFormatter("aabbccddeeff")
        formatted_string = formatter.format()
>       assert formatted_string == "abcdef"
E       AssertionError: assert 'Aabbccddeeff' == 'abcdef'
E         
E         - abcdef
E         + Aabbccddeeff

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py:23: AssertionError
____________________________ test_right_space_only _____________________________

    def test_right_space_only():
        formatter = __StringFormatter("hello,world!this.is.a.test.")
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.'
E       AssertionError: assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py:28: AssertionError
_____________________________ test_left_space_only _____________________________

    def test_left_space_only():
        formatter = __StringFormatter("hello,world!this.is.a.test.")
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.'
E       AssertionError: assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py:33: AssertionError
______________________________ test_spaces_around ______________________________

    def test_spaces_around():
        formatter = __StringFormatter("hello,world!this.is.a.test.")
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.'
E       AssertionError: assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py:38: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py::test_punctuation_and_spacing
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py::test_uppercase_after_sign
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py::test_remove_duplicates
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py::test_right_space_only
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py::test_left_space_only
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_1.py::test_spaces_around
============================== 7 failed in 0.08s ===============================
"""