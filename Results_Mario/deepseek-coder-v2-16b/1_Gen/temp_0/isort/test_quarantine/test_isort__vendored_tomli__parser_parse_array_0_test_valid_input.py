
import pytest
from isort._vendored.tomli._parser import parse_array, suffixed_err

@pytest.mark.parametrize("src, expected", [
    ('[1, 2.5, "string", [3, 4], {"key": "value"}]', [1, 2.5, "string", [3, 4], {"key": "value"}]),
])
def test_valid_input(src: str, expected: list):
    pos = 0
    parse_float = float  # Assuming this function is defined elsewhere to convert string numbers to floats
    final_pos, parsed_array = parse_array(src, pos, parse_float)
    assert parsed_array == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
___ test_valid_input[[1, 2.5, "string", [3, 4], {"key": "value"}]-expected0] ___

src = '[1, 2.5, "string", [3, 4], {"key": "value"}]'
expected = [1, 2.5, 'string', [3, 4], {'key': 'value'}]

    @pytest.mark.parametrize("src, expected", [
        ('[1, 2.5, "string", [3, 4], {"key": "value"}]', [1, 2.5, "string", [3, 4], {"key": "value"}]),
    ])
    def test_valid_input(src: str, expected: list):
        pos = 0
        parse_float = float  # Assuming this function is defined elsewhere to convert string numbers to floats
>       final_pos, parsed_array = parse_array(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:404: in parse_array
    pos, val = parse_value(src, pos, parse_float)
isort/isort/_vendored/tomli/_parser.py:619: in parse_value
    return parse_inline_table(src, pos, parse_float)
isort/isort/_vendored/tomli/_parser.py:429: in parse_inline_table
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '[1, 2.5, "string", [3, 4], {"key": "value"}]', pos = 33
parse_float = <class 'float'>

    def parse_key_value_pair(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, Key, Any]:
        pos, key = parse_key(src, pos)
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char != "=":
>           raise suffixed_err(src, pos, 'Expected "=" after a key in a key/value pair')
E           isort._vendored.tomli._parser.TOMLDecodeError: Expected "=" after a key in a key/value pair (at line 1, column 34)

isort/isort/_vendored/tomli/_parser.py:350: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_valid_input.py::test_valid_input[[1, 2.5, "string", [3, 4], {"key": "value"}]-expected0]
============================== 1 failed in 0.12s ===============================
"""