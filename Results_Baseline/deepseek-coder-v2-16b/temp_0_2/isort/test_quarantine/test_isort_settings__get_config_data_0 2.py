
import pytest
import tomllib
import configparser
import os
from isort.settings import _get_config_data

# Test cases for _get_config_data function
@pytest.mark.parametrize("file_path, sections, expected", [
    ('test/config.toml', ('server', 'database'), dict),
    ('test/settings.editorconfig', ('editor',), dict)
])
def test_get_config_data(file_path, sections, expected):
    config_data = _get_config_data(file_path, sections)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_settings__get_config_data_0.py FF         [100%]

=================================== FAILURES ===================================
____________ test_get_config_data[test/config.toml-sections0-dict] _____________

file_path = 'test/config.toml', sections = ('server', 'database')
expected = <class 'dict'>

    @pytest.mark.parametrize("file_path, sections, expected", [
        ('test/config.toml', ('server', 'database'), dict),
        ('test/settings.editorconfig', ('editor',), dict)
    ])
    def test_get_config_data(file_path, sections, expected):
>       config_data = _get_config_data(file_path, sections)

isort/Test4DT_tests/test_isort_settings__get_config_data_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'test/config.toml', sections = ('server', 'database')

    def _get_config_data(file_path: str, sections: tuple[str, ...]) -> dict[str, Any]:
        settings: dict[str, Any] = {}
    
        if file_path.endswith(".toml"):
>           with open(file_path, "rb") as bin_config_file:
E           FileNotFoundError: [Errno 2] No such file or directory: 'test/config.toml'

isort/isort/settings.py:824: FileNotFoundError
_______ test_get_config_data[test/settings.editorconfig-sections1-dict] ________

file_path = 'test/settings.editorconfig', sections = ('editor',)
expected = <class 'dict'>

    @pytest.mark.parametrize("file_path, sections, expected", [
        ('test/config.toml', ('server', 'database'), dict),
        ('test/settings.editorconfig', ('editor',), dict)
    ])
    def test_get_config_data(file_path, sections, expected):
>       config_data = _get_config_data(file_path, sections)

isort/Test4DT_tests/test_isort_settings__get_config_data_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'test/settings.editorconfig', sections = ('editor',)

    def _get_config_data(file_path: str, sections: tuple[str, ...]) -> dict[str, Any]:
        settings: dict[str, Any] = {}
    
        if file_path.endswith(".toml"):
            with open(file_path, "rb") as bin_config_file:
                config = tomllib.load(bin_config_file)
            for section in sections:
                config_section = config
                for key in section.split("."):
                    config_section = config_section.get(key, {})
                settings.update(config_section)
        else:
>           with open(file_path, encoding="utf-8") as config_file:
E           FileNotFoundError: [Errno 2] No such file or directory: 'test/settings.editorconfig'

isort/isort/settings.py:832: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0.py::test_get_config_data[test/config.toml-sections0-dict]
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0.py::test_get_config_data[test/settings.editorconfig-sections1-dict]
============================== 2 failed in 0.12s ===============================
"""