
import pytest
from isort._vendored.tomli._parser import parse_array, suffixed_err

def test_valid_input():
    src = "[1, 2.0, 'string', true, false, null]"
    pos = 0
    parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    
    expected_pos = len(src)
    expected_array = [1, 2.0, 'string', True, False, None]
    
    parsed_pos, parsed_array = parse_array(src, pos, parse_float)
    
    assert parsed_pos == expected_pos
    assert parsed_array == expected_array

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
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        src = "[1, 2.0, 'string', true, false, null]"
        pos = 0
        parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    
        expected_pos = len(src)
        expected_array = [1, 2.0, 'string', True, False, None]
    
>       parsed_pos, parsed_array = parse_array(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_valid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:404: in parse_array
    pos, val = parse_value(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = "[1, 2.0, 'string', true, false, null]", pos = 32
parse_float = <function test_valid_input.<locals>.<lambda> at 0x7f9c23e298a0>

    def parse_value(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, Any]:  # noqa: C901
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
    
        # Basic strings
        if char == '"':
            if src.startswith('"""', pos):
                return parse_multiline_str(src, pos, literal=False)
            return parse_one_line_basic_str(src, pos)
    
        # Literal strings
        if char == "'":
            if src.startswith("'''", pos):
                return parse_multiline_str(src, pos, literal=True)
            return parse_literal_str(src, pos)
    
        # Booleans
        if char == "t":
            if src.startswith("true", pos):
                return pos + 4, True
        if char == "f":
            if src.startswith("false", pos):
                return pos + 5, False
    
        # Dates and times
        datetime_match = RE_DATETIME.match(src, pos)
        if datetime_match:
            try:
                datetime_obj = match_to_datetime(datetime_match)
            except ValueError:
                raise suffixed_err(src, pos, "Invalid date or datetime")
            return datetime_match.end(), datetime_obj
        localtime_match = RE_LOCALTIME.match(src, pos)
        if localtime_match:
            return localtime_match.end(), match_to_localtime(localtime_match)
    
        # Integers and "normal" floats.
        # The regex will greedily match any type starting with a decimal
        # char, so needs to be located after handling of dates and times.
        number_match = RE_NUMBER.match(src, pos)
        if number_match:
            return number_match.end(), match_to_number(number_match, parse_float)
    
        # Arrays
        if char == "[":
            return parse_array(src, pos, parse_float)
    
        # Inline tables
        if char == "{":
            return parse_inline_table(src, pos, parse_float)
    
        # Special floats
        first_three = src[pos : pos + 3]
        if first_three in {"inf", "nan"}:
            return pos + 3, parse_float(first_three)
        first_four = src[pos : pos + 4]
        if first_four in {"-inf", "+inf", "-nan", "+nan"}:
            return pos + 4, parse_float(first_four)
    
>       raise suffixed_err(src, pos, "Invalid value")
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid value (at line 1, column 33)

isort/isort/_vendored/tomli/_parser.py:629: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.12s ===============================
"""