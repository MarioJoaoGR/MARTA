
import re
from dataclasses_json.stringcase import camelcase, uplowcase
import pytest

@pytest.mark.parametrize("input_string", ["hello_world", "PYTHON programming", "123abc def", "-START-MIDDLE-END-"])
def test_camelcase(input_string):
    expected = re.sub(r"[\-_\.\s]([a-z0-9])", lambda matched: uplowcase(matched.group(1), 'up'), input_string).replace("_", "").replace(" ", "").replace("-", "")
    assert camelcase(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_1_test_error_case_invalid_type.py . [ 25%]
F.F                                                                      [100%]

=================================== FAILURES ===================================
______________________ test_camelcase[PYTHON programming] ______________________

input_string = 'PYTHON programming'

    @pytest.mark.parametrize("input_string", ["hello_world", "PYTHON programming", "123abc def", "-START-MIDDLE-END-"])
    def test_camelcase(input_string):
        expected = re.sub(r"[\-_\.\s]([a-z0-9])", lambda matched: uplowcase(matched.group(1), 'up'), input_string).replace("_", "").replace(" ", "").replace("-", "")
>       assert camelcase(input_string) == expected
E       AssertionError: assert 'pYTHONProgramming' == 'PYTHONProgramming'
E         
E         - PYTHONProgramming
E         ? ^
E         + pYTHONProgramming
E         ? ^

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_1_test_error_case_invalid_type.py:9: AssertionError
______________________ test_camelcase[-START-MIDDLE-END-] ______________________

input_string = '-START-MIDDLE-END-'

    @pytest.mark.parametrize("input_string", ["hello_world", "PYTHON programming", "123abc def", "-START-MIDDLE-END-"])
    def test_camelcase(input_string):
        expected = re.sub(r"[\-_\.\s]([a-z0-9])", lambda matched: uplowcase(matched.group(1), 'up'), input_string).replace("_", "").replace(" ", "").replace("-", "")
>       assert camelcase(input_string) == expected
E       AssertionError: assert 'sTART-MIDDLE-END-' == 'STARTMIDDLEEND'
E         
E         - STARTMIDDLEEND
E         ? ^
E         + sTART-MIDDLE-END-
E         ? ^    +      +   +

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_1_test_error_case_invalid_type.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_1_test_error_case_invalid_type.py::test_camelcase[PYTHON programming]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_1_test_error_case_invalid_type.py::test_camelcase[-START-MIDDLE-END-]
========================= 2 failed, 2 passed in 0.03s ==========================
"""