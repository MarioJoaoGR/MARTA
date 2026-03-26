
import pytest
from isort.settings import Config
from isort.exceptions import ProfileDoesNotExist

@pytest.mark.parametrize("config_overrides", [
    {"quiet": True, "profile": "default"},
    {"indent": 4},
    {"sections": ["known_third_party"]}
])
def test_valid_inputs(config_overrides):
    with pytest.raises(ProfileDoesNotExist):
        Config(**config_overrides)

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

isort/Test4DT_tests/test_isort_settings_Config_section_comments_end_0_test_valid_inputs.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_valid_inputs[config_overrides1] _____________________

config_overrides = {'indent': 4}

    @pytest.mark.parametrize("config_overrides", [
        {"quiet": True, "profile": "default"},
        {"indent": 4},
        {"sections": ["known_third_party"]}
    ])
    def test_valid_inputs(config_overrides):
>       with pytest.raises(ProfileDoesNotExist):
E       Failed: DID NOT RAISE <class 'isort.exceptions.ProfileDoesNotExist'>

isort/Test4DT_tests/test_isort_settings_Config_section_comments_end_0_test_valid_inputs.py:12: Failed
_____________________ test_valid_inputs[config_overrides2] _____________________

config_overrides = {'sections': ['known_third_party']}

    @pytest.mark.parametrize("config_overrides", [
        {"quiet": True, "profile": "default"},
        {"indent": 4},
        {"sections": ["known_third_party"]}
    ])
    def test_valid_inputs(config_overrides):
>       with pytest.raises(ProfileDoesNotExist):
E       Failed: DID NOT RAISE <class 'isort.exceptions.ProfileDoesNotExist'>

isort/Test4DT_tests/test_isort_settings_Config_section_comments_end_0_test_valid_inputs.py:12: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_isort_settings_Config_section_comments_end_0_test_valid_inputs.py::test_valid_inputs[config_overrides2]
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_settings_Config_section_comments_end_0_test_valid_inputs.py:13: UserWarning: `sections` setting includes known_third_party, but no known_known_third_party is defined. The following known_SECTION config options are defined: .
    Config(**config_overrides)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_section_comments_end_0_test_valid_inputs.py::test_valid_inputs[config_overrides1]
FAILED isort/Test4DT_tests/test_isort_settings_Config_section_comments_end_0_test_valid_inputs.py::test_valid_inputs[config_overrides2]
==================== 2 failed, 1 passed, 1 warning in 0.11s ====================
"""