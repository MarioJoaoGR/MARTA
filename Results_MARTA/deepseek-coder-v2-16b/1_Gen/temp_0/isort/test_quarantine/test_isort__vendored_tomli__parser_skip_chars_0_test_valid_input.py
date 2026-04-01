
import pytest
from isort._vendored.tomli._parser import skip_chars

@pytest.mark.parametrize("src, pos, chars, expected", [
    ("hello world", 0, ['l', 'o'], 5),
    ("hello world", 2, ['e', 'h'], 2),
    ("hello world", 4, ['o', 'd'], 7),
    ("hello world", 6, ['w', 'r'], 8),
    ("hello world", 10, ['l', 'o'], 11),
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
collected 5 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py F [ 20%]
.FFF                                                                     [100%]

=================================== FAILURES ===================================
___________________ test_valid_input[hello world-0-chars0-5] ___________________

src = 'hello world', pos = 0, chars = ['l', 'o'], expected = 5

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 8),
        ("hello world", 10, ['l', 'o'], 11),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 0 == 5
E        +  where 0 = skip_chars('hello world', 0, ['l', 'o'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:13: AssertionError
___________________ test_valid_input[hello world-4-chars2-7] ___________________

src = 'hello world', pos = 4, chars = ['o', 'd'], expected = 7

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 8),
        ("hello world", 10, ['l', 'o'], 11),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 5 == 7
E        +  where 5 = skip_chars('hello world', 4, ['o', 'd'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:13: AssertionError
___________________ test_valid_input[hello world-6-chars3-8] ___________________

src = 'hello world', pos = 6, chars = ['w', 'r'], expected = 8

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 8),
        ("hello world", 10, ['l', 'o'], 11),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 7 == 8
E        +  where 7 = skip_chars('hello world', 6, ['w', 'r'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:13: AssertionError
__________________ test_valid_input[hello world-10-chars4-11] __________________

src = 'hello world', pos = 10, chars = ['l', 'o'], expected = 11

    @pytest.mark.parametrize("src, pos, chars, expected", [
        ("hello world", 0, ['l', 'o'], 5),
        ("hello world", 2, ['e', 'h'], 2),
        ("hello world", 4, ['o', 'd'], 7),
        ("hello world", 6, ['w', 'r'], 8),
        ("hello world", 10, ['l', 'o'], 11),
    ])
    def test_valid_input(src, pos, chars, expected):
>       assert skip_chars(src, pos, chars) == expected
E       AssertionError: assert 10 == 11
E        +  where 10 = skip_chars('hello world', 10, ['l', 'o'])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-0-chars0-5]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-4-chars2-7]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-6-chars3-8]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0_test_valid_input.py::test_valid_input[hello world-10-chars4-11]
========================= 4 failed, 1 passed in 0.11s ==========================
"""