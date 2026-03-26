
import pytest
from typing import Tuple, Dict, Callable
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err

# Assuming Pos and ParseFloat are defined elsewhere in the module or imported from a standard library
Pos = int
ParseFloat = Callable[[str], float]

def test_parse_inline_table_simple():
    src = "key = {a=1, b=2}"
    pos = 0
    parse_float = float
    result = parse_inline_table(src, pos, parse_float)
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0.py F [100%]

=================================== FAILURES ===================================
________________________ test_parse_inline_table_simple ________________________

    def test_parse_inline_table_simple():
        src = "key = {a=1, b=2}"
        pos = 0
        parse_float = float
>       result = parse_inline_table(src, pos, parse_float)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'key = {a=1, b=2}', pos = 16, parse_float = <class 'float'>

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
                raise suffixed_err(src, pos, f'Duplicate inline table key "{key_stem}"')
            nest[key_stem] = value
            pos = skip_chars(src, pos, TOML_WS)
            c = src[pos : pos + 1]
            if c == "}":
                return pos + 1, nested_dict.dict
            if c != ",":
>               raise suffixed_err(src, pos, "Unclosed inline table")
E               isort._vendored.tomli._parser.TOMLDecodeError: Unclosed inline table (at end of document)

isort/isort/_vendored/tomli/_parser.py:445: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0.py::test_parse_inline_table_simple
============================== 1 failed in 0.12s ===============================
"""