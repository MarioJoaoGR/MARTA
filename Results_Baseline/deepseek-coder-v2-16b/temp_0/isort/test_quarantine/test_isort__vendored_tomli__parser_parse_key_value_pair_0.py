
import pytest
from typing import Tuple, Any, Optional
from isort._vendored.tomli._parser import parse_key_value_pair, Pos, ParseFloat, Key, TOML_WS

# Assuming suffixed_err and other necessary imports are available in the module
# Also assuming that parse_key, parse_value, skip_chars, and other related functions are defined correctly.

@pytest.mark.parametrize("src, pos, expected_pos, expected_key, expected_value", [
    ('key=value', 0, 4, ('key',), 'value'),
    ('another_key=another_value', 5, 16, ('another_key',), 'another_value'),
    ('number=123.45', 0, 7, ('number',), 123.45),
    ('special_chars=!@#$%^&*()', 0, 16, ('special_chars',), '!@#$%^&*()'),
    ('whitespace key= whitespace value', 0, 19, ('whitespace key',), 'whitespace value'),
])
def test_parse_key_value_pair(src, pos, expected_pos, expected_key, expected_value):
    parse_float = float  # Assuming this is defined elsewhere to convert string numbers to floats
    new_pos, key, value = parse_key_value_pair(src, pos, parse_float)
    
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py F [ 20%]
F.FF                                                                     [100%]

=================================== FAILURES ===================================
_________ test_parse_key_value_pair[key=value-0-4-expected_key0-value] _________

src = 'key=value', pos = 0, expected_pos = 4, expected_key = ('key',)
expected_value = 'value'

    @pytest.mark.parametrize("src, pos, expected_pos, expected_key, expected_value", [
        ('key=value', 0, 4, ('key',), 'value'),
        ('another_key=another_value', 5, 16, ('another_key',), 'another_value'),
        ('number=123.45', 0, 7, ('number',), 123.45),
        ('special_chars=!@#$%^&*()', 0, 16, ('special_chars',), '!@#$%^&*()'),
        ('whitespace key= whitespace value', 0, 19, ('whitespace key',), 'whitespace value'),
    ])
    def test_parse_key_value_pair(src, pos, expected_pos, expected_key, expected_value):
        parse_float = float  # Assuming this is defined elsewhere to convert string numbers to floats
>       new_pos, key, value = parse_key_value_pair(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:353: in parse_key_value_pair
    pos, value = parse_value(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'key=value', pos = 4, parse_float = <class 'float'>

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
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid value (at line 1, column 5)

isort/isort/_vendored/tomli/_parser.py:629: TOMLDecodeError
_ test_parse_key_value_pair[another_key=another_value-5-16-expected_key1-another_value] _

src = 'another_key=another_value', pos = 5, expected_pos = 16
expected_key = ('another_key',), expected_value = 'another_value'

    @pytest.mark.parametrize("src, pos, expected_pos, expected_key, expected_value", [
        ('key=value', 0, 4, ('key',), 'value'),
        ('another_key=another_value', 5, 16, ('another_key',), 'another_value'),
        ('number=123.45', 0, 7, ('number',), 123.45),
        ('special_chars=!@#$%^&*()', 0, 16, ('special_chars',), '!@#$%^&*()'),
        ('whitespace key= whitespace value', 0, 19, ('whitespace key',), 'whitespace value'),
    ])
    def test_parse_key_value_pair(src, pos, expected_pos, expected_key, expected_value):
        parse_float = float  # Assuming this is defined elsewhere to convert string numbers to floats
>       new_pos, key, value = parse_key_value_pair(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:353: in parse_key_value_pair
    pos, value = parse_value(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'another_key=another_value', pos = 12, parse_float = <class 'float'>

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
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid value (at line 1, column 13)

isort/isort/_vendored/tomli/_parser.py:629: TOMLDecodeError
_ test_parse_key_value_pair[special_chars=!@#$%^&*()-0-16-expected_key3-!@#$%^&*()] _

src = 'special_chars=!@#$%^&*()', pos = 0, expected_pos = 16
expected_key = ('special_chars',), expected_value = '!@#$%^&*()'

    @pytest.mark.parametrize("src, pos, expected_pos, expected_key, expected_value", [
        ('key=value', 0, 4, ('key',), 'value'),
        ('another_key=another_value', 5, 16, ('another_key',), 'another_value'),
        ('number=123.45', 0, 7, ('number',), 123.45),
        ('special_chars=!@#$%^&*()', 0, 16, ('special_chars',), '!@#$%^&*()'),
        ('whitespace key= whitespace value', 0, 19, ('whitespace key',), 'whitespace value'),
    ])
    def test_parse_key_value_pair(src, pos, expected_pos, expected_key, expected_value):
        parse_float = float  # Assuming this is defined elsewhere to convert string numbers to floats
>       new_pos, key, value = parse_key_value_pair(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:353: in parse_key_value_pair
    pos, value = parse_value(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'special_chars=!@#$%^&*()', pos = 14, parse_float = <class 'float'>

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
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid value (at line 1, column 15)

isort/isort/_vendored/tomli/_parser.py:629: TOMLDecodeError
_ test_parse_key_value_pair[whitespace key= whitespace value-0-19-expected_key4-whitespace value] _

src = 'whitespace key= whitespace value', pos = 0, expected_pos = 19
expected_key = ('whitespace key',), expected_value = 'whitespace value'

    @pytest.mark.parametrize("src, pos, expected_pos, expected_key, expected_value", [
        ('key=value', 0, 4, ('key',), 'value'),
        ('another_key=another_value', 5, 16, ('another_key',), 'another_value'),
        ('number=123.45', 0, 7, ('number',), 123.45),
        ('special_chars=!@#$%^&*()', 0, 16, ('special_chars',), '!@#$%^&*()'),
        ('whitespace key= whitespace value', 0, 19, ('whitespace key',), 'whitespace value'),
    ])
    def test_parse_key_value_pair(src, pos, expected_pos, expected_key, expected_value):
        parse_float = float  # Assuming this is defined elsewhere to convert string numbers to floats
>       new_pos, key, value = parse_key_value_pair(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'whitespace key= whitespace value', pos = 11
parse_float = <class 'float'>

    def parse_key_value_pair(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, Key, Any]:
        pos, key = parse_key(src, pos)
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char != "=":
>           raise suffixed_err(src, pos, 'Expected "=" after a key in a key/value pair')
E           isort._vendored.tomli._parser.TOMLDecodeError: Expected "=" after a key in a key/value pair (at line 1, column 12)

isort/isort/_vendored/tomli/_parser.py:350: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py::test_parse_key_value_pair[key=value-0-4-expected_key0-value]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py::test_parse_key_value_pair[another_key=another_value-5-16-expected_key1-another_value]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py::test_parse_key_value_pair[special_chars=!@#$%^&*()-0-16-expected_key3-!@#$%^&*()]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0.py::test_parse_key_value_pair[whitespace key= whitespace value-0-19-expected_key4-whitespace value]
========================= 4 failed, 1 passed in 0.15s ==========================
"""