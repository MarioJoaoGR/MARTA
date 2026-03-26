
import pytest
from isort._vendored.tomli._parser import BARE_KEY_CHARS, parse_key_part, suffixed_err
from typing import Optional, Tuple

@pytest.mark.parametrize("src, pos, expected", [
    ("example {'key': 'value'}", 0, (17, "key")),
    ("example {'key': 'value',}", 0, (18, "key")),
    ("example {'key': 'value'", 0, (16, "key")),
])
def test_parse_key_part(src, pos, expected):
    with pytest.raises(suffixed_err) as excinfo:
        parse_key_part(src, pos)
    assert str(excinfo.value) == f"Invalid initial character for a key part (at line 1, column {expected[0]})"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_edge_case_none_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________ test_parse_key_part[example {'key': 'value'}-0-expected0] ___________

src = "example {'key': 'value'}", pos = 0, expected = (17, 'key')

    @pytest.mark.parametrize("src, pos, expected", [
        ("example {'key': 'value'}", 0, (17, "key")),
        ("example {'key': 'value',}", 0, (18, "key")),
        ("example {'key': 'value'", 0, (16, "key")),
    ])
    def test_parse_key_part(src, pos, expected):
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_edge_case_none_input.py:12: TypeError
__________ test_parse_key_part[example {'key': 'value',}-0-expected1] __________

src = "example {'key': 'value',}", pos = 0, expected = (18, 'key')

    @pytest.mark.parametrize("src, pos, expected", [
        ("example {'key': 'value'}", 0, (17, "key")),
        ("example {'key': 'value',}", 0, (18, "key")),
        ("example {'key': 'value'", 0, (16, "key")),
    ])
    def test_parse_key_part(src, pos, expected):
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_edge_case_none_input.py:12: TypeError
___________ test_parse_key_part[example {'key': 'value'-0-expected2] ___________

src = "example {'key': 'value'", pos = 0, expected = (16, 'key')

    @pytest.mark.parametrize("src, pos, expected", [
        ("example {'key': 'value'}", 0, (17, "key")),
        ("example {'key': 'value',}", 0, (18, "key")),
        ("example {'key': 'value'", 0, (16, "key")),
    ])
    def test_parse_key_part(src, pos, expected):
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_edge_case_none_input.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_edge_case_none_input.py::test_parse_key_part[example {'key': 'value'}-0-expected0]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_edge_case_none_input.py::test_parse_key_part[example {'key': 'value',}-0-expected1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_edge_case_none_input.py::test_parse_key_part[example {'key': 'value'-0-expected2]
============================== 3 failed in 0.11s ===============================
"""