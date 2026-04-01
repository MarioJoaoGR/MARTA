
import pytest
from unittest.mock import patch, mock_open
import configparser
import tomllib
import os
from isort.settings import _get_config_data

@pytest.fixture(autouse=True)
def setup():
    pass

@patch('builtins.open', new_callable=mock_open, read_data='[section1]\nkey1 = value1\n[section2]\nkey2 = value2')
def test_get_config_data_from_ini(mock_file):
    config_data = _get_config_data('path/to/editorconfigfile', ('section1', 'section2'))
    assert config_data == {'source': 'path/to/editorconfigfile', 'section1': {'key1': 'value1'}, 'section2': {'key2': 'value2'}}

@patch('builtins.open', new_callable=mock_open, read_data='{ "section1": { "key1": "value1" }, "section2": { "key2": "value2" } }')
def test_get_config_data_from_toml(mock_file):
    config_data = _get_config_data('path/to/tomlfile.toml', ('section1', 'section2'))
    assert config_data == {'source': 'path/to/tomlfile.toml', 'section1': {'key1': 'value1'}, 'section2': {'key2': 'value2'}}

@patch('builtins.open', new_callable=mock_open, read_data='''[section1]
key1 = value1
[section2]
key2 = value2''')
def test_get_config_data_from_ini_with_editorconfig_extension(mock_file):
    config_data = _get_config_data('path/to/editorconfigfile', ('*.{ext}', 'section1'))
    assert config_data == {'source': 'path/to/editorconfigfile', 'section1': {'key1': 'value1'}}

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

isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_edge_cases.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_get_config_data_from_ini _________________________

mock_file = <MagicMock name='open' id='140560237612176'>

    @patch('builtins.open', new_callable=mock_open, read_data='[section1]\nkey1 = value1\n[section2]\nkey2 = value2')
    def test_get_config_data_from_ini(mock_file):
        config_data = _get_config_data('path/to/editorconfigfile', ('section1', 'section2'))
>       assert config_data == {'source': 'path/to/editorconfigfile', 'section1': {'key1': 'value1'}, 'section2': {'key2': 'value2'}}
E       AssertionError: assert {'key1': 'val...orconfigfile'} == {'section1': ...orconfigfile'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 2 more items:
E         {'key1': 'value1', 'key2': 'value2'}
E         Right contains 2 more items:
E         {'section1': {'key1': 'value1'}, 'section2': {'key2': 'value2'}}
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_edge_cases.py:16: AssertionError
________________________ test_get_config_data_from_toml ________________________

mock_file = <MagicMock name='open' id='140560219624400'>

    @patch('builtins.open', new_callable=mock_open, read_data='{ "section1": { "key1": "value1" }, "section2": { "key2": "value2" } }')
    def test_get_config_data_from_toml(mock_file):
>       config_data = _get_config_data('path/to/tomlfile.toml', ('section1', 'section2'))

isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_edge_cases.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:825: in _get_config_data
    config = tomllib.load(bin_config_file)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fp = <MagicMock name='open()' id='140560238017040'>

    def load(fp: BinaryIO, /, *, parse_float: ParseFloat = float) -> dict[str, Any]:
        """Parse TOML from a binary file object."""
        b = fp.read()
        try:
            s = b.decode()
        except AttributeError:
>           raise TypeError(
                "File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`"
            ) from None
E           TypeError: File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`

/usr/local/lib/python3.11/tomllib/_parser.py:63: TypeError
__________ test_get_config_data_from_ini_with_editorconfig_extension ___________

mock_file = <MagicMock name='open' id='140560222944016'>

    @patch('builtins.open', new_callable=mock_open, read_data='''[section1]
    key1 = value1
    [section2]
    key2 = value2''')
    def test_get_config_data_from_ini_with_editorconfig_extension(mock_file):
        config_data = _get_config_data('path/to/editorconfigfile', ('*.{ext}', 'section1'))
>       assert config_data == {'source': 'path/to/editorconfigfile', 'section1': {'key1': 'value1'}}
E       AssertionError: assert {'key1': 'val...orconfigfile'} == {'section1': ...orconfigfile'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'key1': 'value1'}
E         Right contains 1 more item:
E         {'section1': {'key1': 'value1'}}
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_edge_cases.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_edge_cases.py::test_get_config_data_from_ini
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_edge_cases.py::test_get_config_data_from_toml
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_edge_cases.py::test_get_config_data_from_ini_with_editorconfig_extension
============================== 3 failed in 0.17s ===============================
"""