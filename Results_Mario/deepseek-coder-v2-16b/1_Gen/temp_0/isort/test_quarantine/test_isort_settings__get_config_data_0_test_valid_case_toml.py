
import pytest
from isort.settings import _get_config_data
import os
import tomllib
import configparser

@pytest.fixture(params=[("test_config.toml", ("section1", "section2"))])
def valid_toml_file(tmpdir):
    # Create a temporary TOML file for testing
    test_config_path = tmpdir / "test_config.toml"
    with open(test_config_path, "w") as f:
        f.write("[section1]\nkey1=value1\n[section2]\nkey2=value2")
    return str(test_config_path)

def test_valid_case_toml(valid_toml_file):
    config_data = _get_config_data(valid_toml_file, ("section1", "section2"))
    assert config_data == {"key1": "value1", "key2": "value2"}

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

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_toml.py F [100%]

=================================== FAILURES ===================================
____________________ test_valid_case_toml[valid_toml_file0] ____________________

valid_toml_file = '/tmp/pytest-of-joaovitorino/pytest-0/test_valid_case_toml_valid_tom0/test_config.toml'

    def test_valid_case_toml(valid_toml_file):
>       config_data = _get_config_data(valid_toml_file, ("section1", "section2"))

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_toml.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:825: in _get_config_data
    config = tomllib.load(bin_config_file)
/usr/local/lib/python3.11/tomllib/_parser.py:66: in load
    return loads(s, parse_float=parse_float)
/usr/local/lib/python3.11/tomllib/_parser.py:102: in loads
    pos = key_value_rule(src, pos, out, header, parse_float)
/usr/local/lib/python3.11/tomllib/_parser.py:326: in key_value_rule
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
/usr/local/lib/python3.11/tomllib/_parser.py:369: in parse_key_value_pair
    pos, value = parse_value(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '[section1]\nkey1=value1\n[section2]\nkey2=value2', pos = 16
parse_float = <class 'float'>

    def parse_value(  # noqa: C901
        src: str, pos: Pos, parse_float: ParseFloat
    ) -> tuple[Pos, Any]:
        try:
            char: str | None = src[pos]
        except IndexError:
            char = None
    
        # IMPORTANT: order conditions based on speed of checking and likelihood
    
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
    
        # Arrays
        if char == "[":
            return parse_array(src, pos, parse_float)
    
        # Inline tables
        if char == "{":
            return parse_inline_table(src, pos, parse_float)
    
        # Dates and times
        datetime_match = RE_DATETIME.match(src, pos)
        if datetime_match:
            try:
                datetime_obj = match_to_datetime(datetime_match)
            except ValueError as e:
                raise suffixed_err(src, pos, "Invalid date or datetime") from e
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
    
        # Special floats
        first_three = src[pos : pos + 3]
        if first_three in {"inf", "nan"}:
            return pos + 3, parse_float(first_three)
        first_four = src[pos : pos + 4]
        if first_four in {"-inf", "+inf", "-nan", "+nan"}:
            return pos + 4, parse_float(first_four)
    
>       raise suffixed_err(src, pos, "Invalid value")
E       tomllib.TOMLDecodeError: Invalid value (at line 2, column 6)

/usr/local/lib/python3.11/tomllib/_parser.py:649: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_toml.py::test_valid_case_toml[valid_toml_file0]
============================== 1 failed in 0.14s ===============================
"""