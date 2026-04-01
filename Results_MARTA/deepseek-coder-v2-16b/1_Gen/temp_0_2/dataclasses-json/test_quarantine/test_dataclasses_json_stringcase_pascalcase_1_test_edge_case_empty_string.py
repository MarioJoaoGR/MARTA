
import pytest
from dataclasses_json import stringcase

def test_pascalcase_empty_string():
    assert stringcase.pascalcase("") == ""

def test_pascalcase_single_word():
    assert stringcase.pascalcase("hello") == "Hello"

def test_pascalcase_multiple_words():
    assert stringcase.pascalcase("python programming") == "PythonProgramming"

def test_pascalcase_with_numbers():
    assert stringcase.pascalcase("123abc def") == "123AbcDef"

def test_pascalcase_with_special_chars():
    assert stringcase.pascalcase("-START-MIDDLE-END-") == "StartMiddleEnd"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_empty_string.py . [ 20%]
..FF                                                                     [100%]

=================================== FAILURES ===================================
_________________________ test_pascalcase_with_numbers _________________________

    def test_pascalcase_with_numbers():
>       assert stringcase.pascalcase("123abc def") == "123AbcDef"
E       AssertionError: assert '123abcDef' == '123AbcDef'
E         
E         - 123AbcDef
E         ?    ^
E         + 123abcDef
E         ?    ^

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_empty_string.py:15: AssertionError
______________________ test_pascalcase_with_special_chars ______________________

    def test_pascalcase_with_special_chars():
>       assert stringcase.pascalcase("-START-MIDDLE-END-") == "StartMiddleEnd"
E       AssertionError: assert 'START-MIDDLE-END-' == 'StartMiddleEnd'
E         
E         - StartMiddleEnd
E         + START-MIDDLE-END-

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_empty_string.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_empty_string.py::test_pascalcase_with_numbers
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_empty_string.py::test_pascalcase_with_special_chars
========================= 2 failed, 3 passed in 0.03s ==========================
"""