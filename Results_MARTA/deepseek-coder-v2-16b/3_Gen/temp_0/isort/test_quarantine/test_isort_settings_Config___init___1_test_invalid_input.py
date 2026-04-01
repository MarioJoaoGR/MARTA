
import pytest
from isort.settings import Config
from isort.exceptions import InvalidSettingsPath, ProfileDoesNotExist, FormattingPluginDoesNotExist, UnsupportedSettings

def test_invalid_input():
    with pytest.raises(InvalidSettingsPath):
        Config(settings_path="non_existent_file.ini")
    
    with pytest.raises(ProfileDoesNotExist):
        Config(profile="nonexistent_profile")
    
    with pytest.raises(FormattingPluginDoesNotExist):
        Config(formatter="nonexistent_formatter")
    
    # Test unsupported settings
    with pytest.raises(UnsupportedSettings) as exc_info:
        Config(sections=["unsupported_section"])
    
    assert isinstance(exc_info.value, UnsupportedSettings), "Expected UnsupportedSettings to be raised"

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

isort/Test4DT_tests/test_isort_settings_Config___init___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(InvalidSettingsPath):
            Config(settings_path="non_existent_file.ini")
    
        with pytest.raises(ProfileDoesNotExist):
            Config(profile="nonexistent_profile")
    
        with pytest.raises(FormattingPluginDoesNotExist):
            Config(formatter="nonexistent_formatter")
    
        # Test unsupported settings
>       with pytest.raises(UnsupportedSettings) as exc_info:
E       Failed: DID NOT RAISE <class 'isort.exceptions.UnsupportedSettings'>

isort/Test4DT_tests/test_isort_settings_Config___init___1_test_invalid_input.py:17: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_isort_settings_Config___init___1_test_invalid_input.py::test_invalid_input
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_settings_Config___init___1_test_invalid_input.py:18: UserWarning: `sections` setting includes unsupported_section, but no known_unsupported_section is defined. The following known_SECTION config options are defined: .
    Config(sections=["unsupported_section"])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config___init___1_test_invalid_input.py::test_invalid_input
========================= 1 failed, 1 warning in 0.12s =========================
"""