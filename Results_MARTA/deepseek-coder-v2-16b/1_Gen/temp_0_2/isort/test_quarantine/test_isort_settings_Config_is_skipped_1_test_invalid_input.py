
import pytest
from isort.settings import Config, _get_config_data
import os
import tomllib
import posixpath
import fnmatch

@pytest.mark.parametrize("invalid_input", [None, "", "not a path"])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError) as excinfo:
        Config(settings_file=invalid_input)

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

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_1_test_invalid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [None, "", "not a path"])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_1_test_invalid_input.py:11: Failed
_____________________________ test_invalid_input[] _____________________________

invalid_input = ''

    @pytest.mark.parametrize("invalid_input", [None, "", "not a path"])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_1_test_invalid_input.py:11: Failed
________________________ test_invalid_input[not a path] ________________________

invalid_input = 'not a path'

    @pytest.mark.parametrize("invalid_input", [None, "", "not a path"])
    def test_invalid_input(invalid_input):
        with pytest.raises(TypeError) as excinfo:
>           Config(settings_file=invalid_input)

isort/Test4DT_tests/test_isort_settings_Config_is_skipped_1_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'not a path', sections = ('isort', 'tool:isort', 'tool.isort')

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
E           FileNotFoundError: [Errno 2] No such file or directory: 'not a path'

isort/isort/settings.py:832: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_is_skipped_1_test_invalid_input.py::test_invalid_input[None]
FAILED isort/Test4DT_tests/test_isort_settings_Config_is_skipped_1_test_invalid_input.py::test_invalid_input[]
FAILED isort/Test4DT_tests/test_isort_settings_Config_is_skipped_1_test_invalid_input.py::test_invalid_input[not a path]
============================== 3 failed in 0.13s ===============================
"""