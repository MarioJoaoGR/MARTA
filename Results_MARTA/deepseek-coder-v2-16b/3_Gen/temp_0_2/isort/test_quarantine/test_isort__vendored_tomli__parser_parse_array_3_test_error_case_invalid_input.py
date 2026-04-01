
import pytest
from isort._vendored.tomli._parser import parse_array, skip_comments_and_array_ws
from typing import Tuple, Callable, Any

Pos = int
ParseFloat = Callable[[str], float] | None

@pytest.mark.parametrize("src, expected", [
    ("[1, 2, 3]", (7, [1, 2, 3])),
    ("[1.1, 2.2, 3.3]", (14, [1.1, 2.2, 3.3])),
    ('["apple", "banana", "cherry"]', (28, ["apple", "banana", "cherry"])),
    # Add more test cases as needed to cover different scenarios and edge cases
])
def test_parse_array(src: str, expected: Tuple[int, list]):
    pos = 0
    parse_float = float if src.count('.') == 2 else None
    result = parse_array(src, pos, parse_float)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_error_case_invalid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________ test_parse_array[[1, 2, 3]-expected0] _____________________

src = '[1, 2, 3]', expected = (7, [1, 2, 3])

    @pytest.mark.parametrize("src, expected", [
        ("[1, 2, 3]", (7, [1, 2, 3])),
        ("[1.1, 2.2, 3.3]", (14, [1.1, 2.2, 3.3])),
        ('["apple", "banana", "cherry"]', (28, ["apple", "banana", "cherry"])),
        # Add more test cases as needed to cover different scenarios and edge cases
    ])
    def test_parse_array(src: str, expected: Tuple[int, list]):
        pos = 0
        parse_float = float if src.count('.') == 2 else None
        result = parse_array(src, pos, parse_float)
>       assert result == expected
E       assert (9, [1, 2, 3]) == (7, [1, 2, 3])
E         
E         At index 0 diff: 9 != 7
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_error_case_invalid_input.py:19: AssertionError
_________________ test_parse_array[[1.1, 2.2, 3.3]-expected1] __________________

src = '[1.1, 2.2, 3.3]', expected = (14, [1.1, 2.2, 3.3])

    @pytest.mark.parametrize("src, expected", [
        ("[1, 2, 3]", (7, [1, 2, 3])),
        ("[1.1, 2.2, 3.3]", (14, [1.1, 2.2, 3.3])),
        ('["apple", "banana", "cherry"]', (28, ["apple", "banana", "cherry"])),
        # Add more test cases as needed to cover different scenarios and edge cases
    ])
    def test_parse_array(src: str, expected: Tuple[int, list]):
        pos = 0
        parse_float = float if src.count('.') == 2 else None
>       result = parse_array(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_error_case_invalid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:404: in parse_array
    pos, val = parse_value(src, pos, parse_float)
isort/isort/_vendored/tomli/_parser.py:611: in parse_value
    return number_match.end(), match_to_number(number_match, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

match = <re.Match object; span=(1, 4), match='1.1'>, parse_float = None

    def match_to_number(match: "re.Match", parse_float: "ParseFloat") -> Any:
        if match.group("floatpart"):
>           return parse_float(match.group())
E           TypeError: 'NoneType' object is not callable

isort/isort/_vendored/tomli/_re.py:99: TypeError
__________ test_parse_array[["apple", "banana", "cherry"]-expected2] ___________

src = '["apple", "banana", "cherry"]'
expected = (28, ['apple', 'banana', 'cherry'])

    @pytest.mark.parametrize("src, expected", [
        ("[1, 2, 3]", (7, [1, 2, 3])),
        ("[1.1, 2.2, 3.3]", (14, [1.1, 2.2, 3.3])),
        ('["apple", "banana", "cherry"]', (28, ["apple", "banana", "cherry"])),
        # Add more test cases as needed to cover different scenarios and edge cases
    ])
    def test_parse_array(src: str, expected: Tuple[int, list]):
        pos = 0
        parse_float = float if src.count('.') == 2 else None
        result = parse_array(src, pos, parse_float)
>       assert result == expected
E       AssertionError: assert (29, ['apple'...a', 'cherry']) == (28, ['apple'...a', 'cherry'])
E         
E         At index 0 diff: 29 != 28
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_error_case_invalid_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_error_case_invalid_input.py::test_parse_array[[1, 2, 3]-expected0]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_error_case_invalid_input.py::test_parse_array[[1.1, 2.2, 3.3]-expected1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_3_test_error_case_invalid_input.py::test_parse_array[["apple", "banana", "cherry"]-expected2]
============================== 3 failed in 0.13s ===============================
"""