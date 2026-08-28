
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
collected 8 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py F [ 12%]
FFFFFFF                                                                  [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        input_string = 'hello,world!this.is.a.test. Visit us at https://example.com or contact us at info@example.com.'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert '$<uuid>$' in formatted_string, "URLs and emails were not replaced with placeholders."
E       AssertionError: URLs and emails were not replaced with placeholders.
E       assert '$<uuid>$' in 'Hello, world! This. Is. A. Test. Visit us at https://example.com or contact us at info@example.com.'

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:9: AssertionError
________________________ test_url_and_email_replacement ________________________

    def test_url_and_email_replacement():
        input_string = 'Visit us at https://example.com or contact us at info@example.com.'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert '$<uuid>$' in formatted_string, "URLs and emails were not replaced with placeholders."
E       AssertionError: URLs and emails were not replaced with placeholders.
E       assert '$<uuid>$' in 'Visit us at https://example.com or contact us at info@example.com.'

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:16: AssertionError
____________________________ test_remove_duplicates ____________________________

    def test_remove_duplicates():
        input_string = 'helloo,,  world!!'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world!', "Duplicate characters were not removed correctly."
E       AssertionError: Duplicate characters were not removed correctly.
E       assert 'Helloo, world!!' == 'Hello, world!'
E         
E         - Hello, world!
E         + Helloo, world!!
E         ?      +        +

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:22: AssertionError
______________________ test_right_space_after_punctuation ______________________

    def test_right_space_after_punctuation():
        input_string = 'hello,world!this.is.a.test.'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.', "Spaces after punctuation marks were not added correctly."
E       AssertionError: Spaces after punctuation marks were not added correctly.
E       assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:28: AssertionError
______________________ test_left_space_before_punctuation ______________________

    def test_left_space_before_punctuation():
        input_string = 'hello,world!this.is.a.test.'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.', "Spaces before punctuation marks were not added correctly."
E       AssertionError: Spaces before punctuation marks were not added correctly.
E       assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:34: AssertionError
________________________ test_spaces_around_punctuation ________________________

    def test_spaces_around_punctuation():
        input_string = 'hello,world!this.is.a.test.'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello, world! This is a test.', "Spaces around certain punctuation marks were not added correctly."
E       AssertionError: Spaces around certain punctuation marks were not added correctly.
E       assert 'Hello, world... Is. A. Test.' == 'Hello, world...is is a test.'
E         
E         - Hello, world! This is a test.
E         ?                   ^^ ^^^^
E         + Hello, world! This. Is. A. Test.
E         ?                   ^^^ ^^^^^^

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:40: AssertionError
_________________________ test_remove_internal_spaces __________________________

    def test_remove_internal_spaces():
        input_string = 'thi s i s a t est'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert formatted_string == 'This is a test.', "Internal spaces within words were not removed correctly."
E       AssertionError: Internal spaces within words were not removed correctly.
E       assert 'Thi s i s a t est' == 'This is a test.'
E         
E         - This is a test.
E         ?               -
E         + Thi s i s a t est
E         ?    +   +     +

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:46: AssertionError
__________________________ test_uppercase_after_sign ___________________________

    def test_uppercase_after_sign():
        input_string = 'hello:world!this.is.a.test.'
        formatter = __StringFormatter(input_string)
        formatted_string = formatter.format()
>       assert formatted_string == 'Hello: World! This is a test.', "First letter after specific signs was not capitalized correctly."
E       AssertionError: First letter after specific signs was not capitalized correctly.
E       assert 'Hello: world... Is. A. Test.' == 'Hello: World...is is a test.'
E         
E         - Hello: World! This is a test.
E         + Hello: world! This. Is. A. Test.

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py:52: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_url_and_email_replacement
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_remove_duplicates
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_right_space_after_punctuation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_left_space_before_punctuation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_spaces_around_punctuation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_remove_internal_spaces
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter_format_0.py::test_uppercase_after_sign
============================== 8 failed in 0.08s ===============================
"""