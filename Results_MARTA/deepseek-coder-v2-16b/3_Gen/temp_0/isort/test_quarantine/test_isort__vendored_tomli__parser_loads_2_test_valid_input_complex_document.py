
from isort._vendored.tomli._parser import loads
import pytest

def test_valid_input_complex_document():
    toml_document = '''[section]
key=value
number=3.14
list=[1, 2, 3]'''
    
    expected_output = {'section': {'key': 'value', 'number': 3.14, 'list': [1, 2, 3]}}
    
    result = loads(toml_document)
    
    assert result == expected_output

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_loads_2_test_valid_input_complex_document.py F [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_complex_document _______________________

    def test_valid_input_complex_document():
        toml_document = '''[section]
    key=value
    number=3.14
    list=[1, 2, 3]'''
    
        expected_output = {'section': {'key': 'value', 'number': 3.14, 'list': [1, 2, 3]}}
    
>       result = loads(toml_document)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_loads_2_test_valid_input_complex_document.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:101: in loads
    pos = key_value_rule(src, pos, out, header, parse_float)
isort/isort/_vendored/tomli/_parser.py:322: in key_value_rule
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
isort/isort/_vendored/tomli/_parser.py:353: in parse_key_value_pair
    pos, value = parse_value(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '[section]\nkey=value\nnumber=3.14\nlist=[1, 2, 3]', pos = 14
parse_float = <class 'float'>

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
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid value (at line 2, column 5)

isort/isort/_vendored/tomli/_parser.py:629: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_loads_2_test_valid_input_complex_document.py::test_valid_input_complex_document
============================== 1 failed in 0.15s ===============================
"""