
import os
import pytest
import tomlkit
from semantic_release.settings import _config_from_pyproject


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_pyproject_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Ensure there is a valid pyproject.toml file at the specified path
        config = _config_from_pyproject("tests/test_pyproject.toml")
        assert isinstance(config, dict)
>       assert "tool" in config
E       AssertionError: assert 'tool' in {}

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_pyproject_0.py:11: AssertionError
______________________________ test_invalid_toml _______________________________

    def test_invalid_toml():
        # Ensure the pyproject.toml file contains invalid TOML syntax
>       with pytest.raises(tomlkit.exceptions.TOMLKitError):
E       Failed: DID NOT RAISE <class 'tomlkit.exceptions.TOMLKitError'>

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_pyproject_0.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_pyproject_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_pyproject_0.py::test_invalid_toml
============================== 2 failed in 0.06s ===============================
"""