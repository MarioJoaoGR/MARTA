
import pytest
from isort.settings import Config
from unittest.mock import patch

@pytest.fixture
def config():
    return Config(settings_file="path/to/config.ini")

def test_is_skipped_with_valid_input(config):
    with patch('os.path.isfile', return_value=True), \
         patch('os.path.isdir', return_value=False), \
         patch('os.path.islink', return_value=False):
        assert not config.is_skipped("valid/path/to/file")

def test_is_skipped_with_invalid_input(config):
    with patch('os.path.isfile', return_value=False), \
         patch('os.path.isdir', return_value=True), \
         patch('os.path.islink', return_value=False):
        assert config.is_skipped("invalid/path/to/directory")

def test_is_skipped_with_non_existent_input(config):
    with patch('os.path.isfile', return_value=False), \
         patch('os.path.isdir', return_value=False), \
         patch('os.path.islink', return_value=True):
        assert config.is_skipped("non/existent/path")

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

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_valid_input.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
______________ ERROR at setup of test_is_skipped_with_valid_input ______________

    @pytest.fixture
    def config():
>       return Config(settings_file="path/to/config.ini")

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'path/to/config.ini'
sections = ('isort', 'tool:isort', 'tool.isort')

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
E           FileNotFoundError: [Errno 2] No such file or directory: 'path/to/config.ini'

isort/isort/settings.py:832: FileNotFoundError
_____________ ERROR at setup of test_is_skipped_with_invalid_input _____________

    @pytest.fixture
    def config():
>       return Config(settings_file="path/to/config.ini")

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'path/to/config.ini'
sections = ('isort', 'tool:isort', 'tool.isort')

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
E           FileNotFoundError: [Errno 2] No such file or directory: 'path/to/config.ini'

isort/isort/settings.py:832: FileNotFoundError
__________ ERROR at setup of test_is_skipped_with_non_existent_input ___________

    @pytest.fixture
    def config():
>       return Config(settings_file="path/to/config.ini")

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'path/to/config.ini'
sections = ('isort', 'tool:isort', 'tool.isort')

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
E           FileNotFoundError: [Errno 2] No such file or directory: 'path/to/config.ini'

isort/isort/settings.py:832: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_valid_input.py::test_is_skipped_with_valid_input
ERROR isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_valid_input.py::test_is_skipped_with_invalid_input
ERROR isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_valid_input.py::test_is_skipped_with_non_existent_input
============================== 3 errors in 0.17s ===============================
"""