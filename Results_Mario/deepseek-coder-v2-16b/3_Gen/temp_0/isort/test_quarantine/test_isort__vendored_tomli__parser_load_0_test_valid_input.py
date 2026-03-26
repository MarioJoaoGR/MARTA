
import pytest
from io import BytesIO
from isort._vendored.tomli._parser import load, loads
from typing import Dict, Any, IO, Callable

def test_valid_input():
    toml_document = b"key=value"
    fp = BytesIO(toml_document)
    result = load(fp)
    assert isinstance(result, dict), "The result should be a dictionary."
    assert result == {'key': 'value'}, "The parsed content is incorrect."

def test_custom_float_parser():
    def custom_float_parser(s):
        return float(s.replace('*', ''))
    
    toml_document = b"number=3.14*"
    fp = BytesIO(toml_document)
    result = load(fp, parse_float=custom_float_parser)
    assert isinstance(result['number'], float), "The number should be a float."
    assert result['number'] == 3.14, "The parsed number is incorrect after custom parsing."

def test_deprecated_text_file_warning():
    toml_document = "key=value"
    fp = BytesIO(toml_document.encode())
    
    with pytest.warns(DeprecationWarning):
        load(fp)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        toml_document = b"key=value"
        fp = BytesIO(toml_document)
>       result = load(fp)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:66: in load
    return loads(s, parse_float=parse_float)
isort/isort/_vendored/tomli/_parser.py:101: in loads
    pos = key_value_rule(src, pos, out, header, parse_float)
isort/isort/_vendored/tomli/_parser.py:322: in key_value_rule
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
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
___________________________ test_custom_float_parser ___________________________

    def test_custom_float_parser():
        def custom_float_parser(s):
            return float(s.replace('*', ''))
    
        toml_document = b"number=3.14*"
        fp = BytesIO(toml_document)
>       result = load(fp, parse_float=custom_float_parser)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:66: in load
    return loads(s, parse_float=parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 'number=3.14*'

    def loads(s: str, *, parse_float: ParseFloat = float) -> Dict[str, Any]:  # noqa: C901
        """Parse TOML from a string."""
    
        # The spec allows converting "\r\n" to "\n", even in string
        # literals. Let's do so to simplify parsing.
        src = s.replace("\r\n", "\n")
        pos = 0
        out = Output(NestedDict(), Flags())
        header: Key = ()
    
        # Parse one statement at a time
        # (typically means one line in TOML source)
        while True:
            # 1. Skip line leading whitespace
            pos = skip_chars(src, pos, TOML_WS)
    
            # 2. Parse rules. Expect one of the following:
            #    - end of file
            #    - end of line
            #    - comment
            #    - key/value pair
            #    - append dict to list (and move to its namespace)
            #    - create dict (and move to its namespace)
            # Skip trailing whitespace when applicable.
            try:
                char = src[pos]
            except IndexError:
                break
            if char == "\n":
                pos += 1
                continue
            if char in KEY_INITIAL_CHARS:
                pos = key_value_rule(src, pos, out, header, parse_float)
                pos = skip_chars(src, pos, TOML_WS)
            elif char == "[":
                try:
                    second_char: Optional[str] = src[pos + 1]
                except IndexError:
                    second_char = None
                if second_char == "[":
                    pos, header = create_list_rule(src, pos, out)
                else:
                    pos, header = create_dict_rule(src, pos, out)
                pos = skip_chars(src, pos, TOML_WS)
            elif char != "#":
                raise suffixed_err(src, pos, "Invalid statement")
    
            # 3. Skip comment
            pos = skip_comment(src, pos)
    
            # 4. Expect end of line or end of file
            try:
                char = src[pos]
            except IndexError:
                break
            if char != "\n":
>               raise suffixed_err(src, pos, "Expected newline or end of document after a statement")
E               isort._vendored.tomli._parser.TOMLDecodeError: Expected newline or end of document after a statement (at line 1, column 12)

isort/isort/_vendored/tomli/_parser.py:125: TOMLDecodeError
______________________ test_deprecated_text_file_warning _______________________

    def test_deprecated_text_file_warning():
        toml_document = "key=value"
        fp = BytesIO(toml_document.encode())
    
        with pytest.warns(DeprecationWarning):
>           load(fp)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:66: in load
    return loads(s, parse_float=parse_float)
isort/isort/_vendored/tomli/_parser.py:101: in loads
    pos = key_value_rule(src, pos, out, header, parse_float)
isort/isort/_vendored/tomli/_parser.py:322: in key_value_rule
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
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

During handling of the above exception, another exception occurred:

    def test_deprecated_text_file_warning():
        toml_document = "key=value"
        fp = BytesIO(toml_document.encode())
    
>       with pytest.warns(DeprecationWarning):
E       Failed: DID NOT WARN. No warnings of type (<class 'DeprecationWarning'>,) were emitted.
E        Emitted warnings: [].

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:28: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py::test_valid_input
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py::test_custom_float_parser
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py::test_deprecated_text_file_warning
============================== 3 failed in 0.23s ===============================
"""