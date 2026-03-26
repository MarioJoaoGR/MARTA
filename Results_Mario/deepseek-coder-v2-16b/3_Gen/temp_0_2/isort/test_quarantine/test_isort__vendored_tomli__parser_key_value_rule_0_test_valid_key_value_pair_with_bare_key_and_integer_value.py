
import pytest
from isort._vendored.tomli._parser import key_value_rule, Output, Key, ParseFloat

@pytest.mark.parametrize("src, pos, expected_pos", [
    ("key=42", 0, len("key=42")),
    ('"hello"=42', 0, len('"hello"=42')),
    ('"pi"=3.14', 0, len('"pi"=3.14'))
])
def test_valid_key_value_pair_with_bare_key_and_integer_value(src, pos, expected_pos):
    out = Output()
    header = ()
    parse_float = float
    
    new_pos = key_value_rule(src, pos, out, header, parse_float)
    
    assert new_pos == expected_pos

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_key_value_pair_with_bare_key_and_integer_value.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____ test_valid_key_value_pair_with_bare_key_and_integer_value[key=42-0-6] _____

src = 'key=42', pos = 0, expected_pos = 6

    @pytest.mark.parametrize("src, pos, expected_pos", [
        ("key=42", 0, len("key=42")),
        ('"hello"=42', 0, len('"hello"=42')),
        ('"pi"=3.14', 0, len('"pi"=3.14'))
    ])
    def test_valid_key_value_pair_with_bare_key_and_integer_value(src, pos, expected_pos):
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_key_value_pair_with_bare_key_and_integer_value.py:11: TypeError
__ test_valid_key_value_pair_with_bare_key_and_integer_value["hello"=42-0-10] __

src = '"hello"=42', pos = 0, expected_pos = 10

    @pytest.mark.parametrize("src, pos, expected_pos", [
        ("key=42", 0, len("key=42")),
        ('"hello"=42', 0, len('"hello"=42')),
        ('"pi"=3.14', 0, len('"pi"=3.14'))
    ])
    def test_valid_key_value_pair_with_bare_key_and_integer_value(src, pos, expected_pos):
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_key_value_pair_with_bare_key_and_integer_value.py:11: TypeError
___ test_valid_key_value_pair_with_bare_key_and_integer_value["pi"=3.14-0-9] ___

src = '"pi"=3.14', pos = 0, expected_pos = 9

    @pytest.mark.parametrize("src, pos, expected_pos", [
        ("key=42", 0, len("key=42")),
        ('"hello"=42', 0, len('"hello"=42')),
        ('"pi"=3.14', 0, len('"pi"=3.14'))
    ])
    def test_valid_key_value_pair_with_bare_key_and_integer_value(src, pos, expected_pos):
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_key_value_pair_with_bare_key_and_integer_value.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_key_value_pair_with_bare_key_and_integer_value.py::test_valid_key_value_pair_with_bare_key_and_integer_value[key=42-0-6]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_key_value_pair_with_bare_key_and_integer_value.py::test_valid_key_value_pair_with_bare_key_and_integer_value["hello"=42-0-10]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_key_value_pair_with_bare_key_and_integer_value.py::test_valid_key_value_pair_with_bare_key_and_integer_value["pi"=3.14-0-9]
============================== 3 failed in 0.16s ===============================
"""