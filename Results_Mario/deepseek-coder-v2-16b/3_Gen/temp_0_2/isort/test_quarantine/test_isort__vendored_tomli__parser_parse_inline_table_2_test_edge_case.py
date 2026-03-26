
import pytest
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err

def test_parse_inline_table():
    # Test case for a simple inline table with string and float values
    input_str = "{key1= 'value1', key2= 3.14}"
    expected = {'key1': 'value1', 'key2': 3.14}
    result = parse_inline_table(input_str, 0, float)
    assert result[1] == expected

    # Test case for an inline table without trailing comma should be parsed correctly
    input_str = "{key1= 'value1', key2= 3.14, }"
    expected = {'key1': 'value1', 'key2': 3.14}
    result = parse_inline_table(input_str, 0, float)
    assert result[1] == expected

    # Test case for a nested inline table
    input_str = "{key1= 'value1', key2= 3.14, key3= {}}"
    expected = {'key1': 'value1', 'key2': 3.14, 'key3': {}}
    result = parse_inline_table(input_str, 0, float)
    assert result[1] == expected

    # Test case for an empty inline table
    input_str = "{}"
    expected = {}
    result = parse_inline_table(input_str, 0, float)
    assert result[1] == expected

    # Test case to check error handling for unclosed inline table
    input_str = "{key1= 'value1', key2= 3.14"
    with pytest.raises(suffixed_err):
        parse_inline_table(input_str, 0, float)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
___________________________ test_parse_inline_table ____________________________

    def test_parse_inline_table():
        # Test case for a simple inline table with string and float values
        input_str = "{key1= 'value1', key2= 3.14}"
        expected = {'key1': 'value1', 'key2': 3.14}
        result = parse_inline_table(input_str, 0, float)
        assert result[1] == expected
    
        # Test case for an inline table without trailing comma should be parsed correctly
        input_str = "{key1= 'value1', key2= 3.14, }"
        expected = {'key1': 'value1', 'key2': 3.14}
>       result = parse_inline_table(input_str, 0, float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_2_test_edge_case.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:429: in parse_inline_table
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
isort/isort/_vendored/tomli/_parser.py:344: in parse_key_value_pair
    pos, key = parse_key(src, pos)
isort/isort/_vendored/tomli/_parser.py:358: in parse_key
    pos, key_part = parse_key_part(src, pos)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = "{key1= 'value1', key2= 3.14, }", pos = 29

    def parse_key_part(src: str, pos: Pos) -> Tuple[Pos, str]:
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char in BARE_KEY_CHARS:
            start_pos = pos
            pos = skip_chars(src, pos, BARE_KEY_CHARS)
            return pos, src[start_pos:pos]
        if char == "'":
            return parse_literal_str(src, pos)
        if char == '"':
            return parse_one_line_basic_str(src, pos)
>       raise suffixed_err(src, pos, "Invalid initial character for a key part")
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid initial character for a key part (at line 1, column 30)

isort/isort/_vendored/tomli/_parser.py:388: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_2_test_edge_case.py::test_parse_inline_table
============================== 1 failed in 0.15s ===============================
"""