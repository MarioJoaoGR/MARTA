
import pytest
from isort._vendored.tomli._parser import parse_key_part, BARE_KEY_CHARS

def test_parse_key_part_basic():
    # Test parsing a bare key part
    src = "hello_world"
    pos = 0
    new_pos, key_part = parse_key_part(src, pos)
    assert new_pos == len("hello_world")
    assert key_part == "hello_world"
    
    # Test parsing a single-quoted string literal
    src = "'hello world'"
    pos = 0
    new_pos, lit_str = parse_key_part(src, pos)
    assert new_pos == len("'hello world'")
    assert lit_str == "hello world"
    
    # Test parsing a double-quoted string literal
    src = '"hello world"'
    pos = 0
    new_pos, lit_str = parse_key_part(src, pos)
    assert new_pos == len('"hello world"')
    assert lit_str == "hello world"
    
    # Test handling an invalid key part
    src = "invalid#key"
    pos = 0
    with pytest.raises(ValueError):
        parse_key_part(src, pos)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_parse_key_part_basic.py F [100%]

=================================== FAILURES ===================================
__________________________ test_parse_key_part_basic ___________________________

    def test_parse_key_part_basic():
        # Test parsing a bare key part
        src = "hello_world"
        pos = 0
        new_pos, key_part = parse_key_part(src, pos)
        assert new_pos == len("hello_world")
        assert key_part == "hello_world"
    
        # Test parsing a single-quoted string literal
        src = "'hello world'"
        pos = 0
        new_pos, lit_str = parse_key_part(src, pos)
        assert new_pos == len("'hello world'")
        assert lit_str == "hello world"
    
        # Test parsing a double-quoted string literal
        src = '"hello world"'
        pos = 0
        new_pos, lit_str = parse_key_part(src, pos)
        assert new_pos == len('"hello world"')
        assert lit_str == "hello world"
    
        # Test handling an invalid key part
        src = "invalid#key"
        pos = 0
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_parse_key_part_basic.py:30: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_parse_key_part_basic.py::test_parse_key_part_basic
============================== 1 failed in 0.10s ===============================
"""