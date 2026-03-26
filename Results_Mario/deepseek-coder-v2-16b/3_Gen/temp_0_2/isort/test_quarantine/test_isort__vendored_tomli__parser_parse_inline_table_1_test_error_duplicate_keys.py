
from isort._vendored.tomli._parser import parse_inline_table, Pos, ParseFloat
import pytest
from typing import Tuple, Dict

# Mocking necessary types for the test
class NestedDict:
    def __init__(self):
        self.dict = {}
    
    def get_or_create_nest(self, key_parent: str, access_lists: bool):
        if key_parent not in self.dict:
            raise KeyError("Key not found")
        return self.dict[key_parent]

class Flags:
    FROZEN = "frozen"
    
    @staticmethod
    def is_(key, flag):
        return False
    
    @staticmethod
    def set(key, flag, recursive=False):
        pass

# Mocking the error for testing
class suffixed_err(Exception):
    def __init__(self, src, pos, msg):
        self.message = msg

def skip_chars(src: str, pos: int, pattern: str) -> int:
    while pos < len(src) and src[pos] in pattern:
        pos += 1
    return pos

# Test case for duplicate keys error in inline table
@pytest.mark.parametrize("src", ["{key1= 'value1', key2= 3.14, key1= 'newValue'}"])
def test_error_duplicate_keys(src):
    with pytest.raises(suffixed_err) as excinfo:
        pos = 0
        parse_float = float
        result = parse_inline_table(src, pos, parse_float)
    assert "Duplicate inline table key" in str(excinfo.value)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_1_test_error_duplicate_keys.py F [100%]

=================================== FAILURES ===================================
__ test_error_duplicate_keys[{key1= 'value1', key2= 3.14, key1= 'newValue'}] ___

src = "{key1= 'value1', key2= 3.14, key1= 'newValue'}"

    @pytest.mark.parametrize("src", ["{key1= 'value1', key2= 3.14, key1= 'newValue'}"])
    def test_error_duplicate_keys(src):
        with pytest.raises(suffixed_err) as excinfo:
            pos = 0
            parse_float = float
>           result = parse_inline_table(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_1_test_error_duplicate_keys.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = "{key1= 'value1', key2= 3.14, key1= 'newValue'}", pos = 45
parse_float = <class 'float'>

    def parse_inline_table(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, dict]:
        pos += 1
        nested_dict = NestedDict()
        flags = Flags()
    
        pos = skip_chars(src, pos, TOML_WS)
        if src.startswith("}", pos):
            return pos + 1, nested_dict.dict
        while True:
            pos, key, value = parse_key_value_pair(src, pos, parse_float)
            key_parent, key_stem = key[:-1], key[-1]
            if flags.is_(key, Flags.FROZEN):
                raise suffixed_err(src, pos, f"Can not mutate immutable namespace {key}")
            try:
                nest = nested_dict.get_or_create_nest(key_parent, access_lists=False)
            except KeyError:
                raise suffixed_err(src, pos, "Can not overwrite a value")
            if key_stem in nest:
>               raise suffixed_err(src, pos, f'Duplicate inline table key "{key_stem}"')
E               isort._vendored.tomli._parser.TOMLDecodeError: Duplicate inline table key "key1" (at line 1, column 46)

isort/isort/_vendored/tomli/_parser.py:438: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_1_test_error_duplicate_keys.py::test_error_duplicate_keys[{key1= 'value1', key2= 3.14, key1= 'newValue'}]
============================== 1 failed in 0.12s ===============================
"""