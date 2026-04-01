
import pytest
from isort._vendored.tomli._parser import load as toml_load
from io import StringIO
import warnings

def test_invalid_input_text_mode():
    with open('example.toml', 'w') as file:
        file.write("invalid_content")
    
    with open('example.toml', 'r') as file:
        fp = file
        with pytest.warns(DeprecationWarning):
            with warnings.catch_warnings():
                # Cause all warnings to be triggered.
                warnings.simplefilter("always")
                data = toml_load(fp)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_2_test_invalid_input_text_mode.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_input_text_mode _________________________

    def test_invalid_input_text_mode():
        with open('example.toml', 'w') as file:
            file.write("invalid_content")
    
        with open('example.toml', 'r') as file:
            fp = file
            with pytest.warns(DeprecationWarning):
                with warnings.catch_warnings():
                    # Cause all warnings to be triggered.
                    warnings.simplefilter("always")
>                   data = toml_load(fp)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_2_test_invalid_input_text_mode.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:66: in load
    return loads(s, parse_float=parse_float)
isort/isort/_vendored/tomli/_parser.py:101: in loads
    pos = key_value_rule(src, pos, out, header, parse_float)
isort/isort/_vendored/tomli/_parser.py:322: in key_value_rule
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'invalid_content', pos = 15, parse_float = <class 'float'>

    def parse_key_value_pair(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, Key, Any]:
        pos, key = parse_key(src, pos)
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char != "=":
>           raise suffixed_err(src, pos, 'Expected "=" after a key in a key/value pair')
E           isort._vendored.tomli._parser.TOMLDecodeError: Expected "=" after a key in a key/value pair (at end of document)

isort/isort/_vendored/tomli/_parser.py:350: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_2_test_invalid_input_text_mode.py::test_invalid_input_text_mode
============================== 1 failed in 0.14s ===============================
"""