
# Module: isort.settings
# test_isort_config.py
from isort import Config, sorting  # Importing sorting module to access sorting functions
import pytest
from isort.exceptions import UnsupportedSettings, ProfileDoesNotExist, SortingFunctionDoesNotExist

def test_init_with_settings_file():
    with pytest.raises(FileNotFoundError):
        config = Config(settings_file="custom_settings.ini")

def test_init_with_settings_file_and_overrides():
    with pytest.raises(FileNotFoundError):
        config = Config(settings_file="custom_settings.ini", sort_order="natural")

def test_handle_deprecated_options():
    with pytest.raises(UnsupportedSettings):
        config = Config(settings_file="custom_settings.ini", old_option=True)

def test_specify_profile_and_configuration_overrides():
    with pytest.raises(FileNotFoundError):
        config = Config(settings_file="custom_settings.ini", profile="black")

def test_handle_profile_does_not_exist_exception():
    with pytest.raises(ProfileDoesNotExist):
        config = Config(settings_file="custom_settings.ini", profile="non_existent_profile")

def test_sorting_function_natural():
    config = Config()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0.py ..F [ 50%]
.F.                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_handle_deprecated_options ________________________

    def test_handle_deprecated_options():
        with pytest.raises(UnsupportedSettings):
>           config = Config(settings_file="custom_settings.ini", old_option=True)

isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'custom_settings.ini'
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
E           FileNotFoundError: [Errno 2] No such file or directory: 'custom_settings.ini'

isort/isort/settings.py:832: FileNotFoundError
_________________ test_handle_profile_does_not_exist_exception _________________

    def test_handle_profile_does_not_exist_exception():
        with pytest.raises(ProfileDoesNotExist):
>           config = Config(settings_file="custom_settings.ini", profile="non_existent_profile")

isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'custom_settings.ini'
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
E           FileNotFoundError: [Errno 2] No such file or directory: 'custom_settings.ini'

isort/isort/settings.py:832: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0.py::test_handle_deprecated_options
FAILED isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0.py::test_handle_profile_does_not_exist_exception
========================= 2 failed, 4 passed in 0.13s ==========================
"""