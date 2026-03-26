
import pytest
from isort._vendored.tomli._parser import skip_chars

@pytest.mark.parametrize("src, pos, chars, expected", [
    ("hello world", 0, ['l', 'o'], 5),
    ("hello world", 2, ['e', 'h'], 2),
    ("hello world", 4, ['o', 'd'], 7),
    ("hello world", 6, ['w', 'r'], 6),
    ("hello world", 0, ['l', 'x'], 1),
    ("hello world", 0, [], 0),
])
def test_valid_input(src, pos, chars, expected):
    assert skip_chars(src, pos, chars) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py F [ 16%]
.FFF.                                                                    [100%]

=================================== FAILURES ===================================
___________________ test_valid_input[hello world-0-chars0-5] ___________________

src = 'hello world', pos = 0, chars = ['l', 'o'], expected = 5

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 6),
        ("hello world", 0, ['l', 'x'], 1),
        ("hello world", 0, [], 0),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 0 == 5
E        +  where 0 = skip_chars('hello world', 0, ['l', 'o'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:14: AssertionError
___________________ test_valid_input[hello world-4-chars2-7] ___________________

src = 'hello world', pos = 4, chars = ['o', 'd'], expected = 7

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 6),
        ("hello world", 0, ['l', 'x'], 1),
        ("hello world", 0, [], 0),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 5 == 7
E        +  where 5 = skip_chars('hello world', 4, ['o', 'd'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:14: AssertionError
___________________ test_valid_input[hello world-6-chars3-6] ___________________

src = 'hello world', pos = 6, chars = ['w', 'r'], expected = 6

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 6),
        ("hello world", 0, ['l', 'x'], 1),
        ("hello world", 0, [], 0),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 7 == 6
E        +  where 7 = skip_chars('hello world', 6, ['w', 'r'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:14: AssertionError
___________________ test_valid_input[hello world-0-chars4-1] ___________________

src = 'hello world', pos = 0, chars = ['l', 'x'], expected = 1

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 6),
        ("hello world", 0, ['l', 'x'], 1),
        ("hello world", 0, [], 0),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 0 == 1
E        +  where 0 = skip_chars('hello world', 0, ['l', 'x'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-0-chars0-5]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-4-chars2-7]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-6-chars3-6]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-0-chars4-1]
========================= 4 failed, 2 passed in 0.13s ==========================
"""