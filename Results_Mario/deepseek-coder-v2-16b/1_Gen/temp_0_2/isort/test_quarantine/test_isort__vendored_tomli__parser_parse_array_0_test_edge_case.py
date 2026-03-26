
import pytest
from isort._vendored.tomli._parser import parse_array, Pos, ParseFloat

def test_parse_empty_array():
    src = "[]"
    pos = 0
    parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    parsed_pos, parsed_array = parse_array(src, pos, parse_float)
    assert parsed_pos == len(src)
    assert parsed_array == []

def test_parse_single_element_array():
    src = "[123]"
    pos = 0
    parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    parsed_pos, parsed_array = parse_array(src, pos, parse_float)
    assert parsed_pos == len(src)
    assert parsed_array == [123]

def test_parse_multiple_element_array():
    src = "[123, 456, \"789.0\"]"
    pos = 0
    parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    parsed_pos, parsed_array = parse_array(src, pos, parse_float)
    assert parsed_pos == len(src)
    assert parsed_array == [123, 456, 789.0]

def test_parse_nested_arrays():
    src = "[[1, 2], [3, 4]]"
    pos = 0
    parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    parsed_pos, parsed_array = parse_array(src, pos, parse_float)
    assert parsed_pos == len(src)
    assert parsed_array == [[1, 2], [3, 4]]

def test_parse_array_with_comments():
    src = "[// comment\n1]"
    pos = 0
    parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    parsed_pos, parsed_array = parse_array(src, pos, parse_float)
    assert parsed_pos == len(src)
    assert parsed_array == [1]

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_edge_case.py . [ 20%]
.F.F                                                                     [100%]

=================================== FAILURES ===================================
______________________ test_parse_multiple_element_array _______________________

    def test_parse_multiple_element_array():
        src = "[123, 456, \"789.0\"]"
        pos = 0
        parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
        parsed_pos, parsed_array = parse_array(src, pos, parse_float)
        assert parsed_pos == len(src)
>       assert parsed_array == [123, 456, 789.0]
E       AssertionError: assert [123, 456, '789.0'] == [123, 456, 789.0]
E         
E         At index 2 diff: '789.0' != 789.0
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_edge_case.py:27: AssertionError
________________________ test_parse_array_with_comments ________________________

    def test_parse_array_with_comments():
        src = "[// comment\n1]"
        pos = 0
        parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
>       parsed_pos, parsed_array = parse_array(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_edge_case.py:41: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:404: in parse_array
    pos, val = parse_value(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '[// comment\n1]', pos = 1
parse_float = <function test_parse_array_with_comments.<locals>.<lambda> at 0x7fea0a188400>

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
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid value (at line 1, column 2)

isort/isort/_vendored/tomli/_parser.py:629: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_edge_case.py::test_parse_multiple_element_array
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_edge_case.py::test_parse_array_with_comments
========================= 2 failed, 3 passed in 0.14s ==========================
"""