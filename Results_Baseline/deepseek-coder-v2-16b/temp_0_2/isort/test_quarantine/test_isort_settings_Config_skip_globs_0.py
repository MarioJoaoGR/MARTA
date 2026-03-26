
import pytest
from isort.settings import Config
import os
from warnings import warn

@pytest.fixture
def config():
    return Config()

@pytest.fixture
def custom_config():
    return Config(config=Config(), quiet=True)

# Test initialization with settings_file parameter
def test_init_with_settings_file(tmpdir):
    settings_file = tmpdir / "custom_config.toml"
    settings_file.write("dummy content")
    config = Config(settings_file=str(settings_file))
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

isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0.py F         [100%]

=================================== FAILURES ===================================
_________________________ test_init_with_settings_file _________________________

tmpdir = local('/tmp/pytest-of-joaovitorino/pytest-10/test_init_with_settings_file0')

    def test_init_with_settings_file(tmpdir):
        settings_file = tmpdir / "custom_config.toml"
        settings_file.write("dummy content")
>       config = Config(settings_file=str(settings_file))

isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
isort/isort/settings.py:825: in _get_config_data
    config = tomllib.load(bin_config_file)
/usr/local/lib/python3.11/tomllib/_parser.py:66: in load
    return loads(s, parse_float=parse_float)
/usr/local/lib/python3.11/tomllib/_parser.py:102: in loads
    pos = key_value_rule(src, pos, out, header, parse_float)
/usr/local/lib/python3.11/tomllib/_parser.py:326: in key_value_rule
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'dummy content', pos = 6, parse_float = <class 'float'>

    def parse_key_value_pair(
        src: str, pos: Pos, parse_float: ParseFloat
    ) -> tuple[Pos, Key, Any]:
        pos, key = parse_key(src, pos)
        try:
            char: str | None = src[pos]
        except IndexError:
            char = None
        if char != "=":
>           raise suffixed_err(src, pos, "Expected '=' after a key in a key/value pair")
E           tomllib.TOMLDecodeError: Expected '=' after a key in a key/value pair (at line 1, column 7)

/usr/local/lib/python3.11/tomllib/_parser.py:366: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0.py::test_init_with_settings_file
============================== 1 failed in 0.14s ===============================
"""