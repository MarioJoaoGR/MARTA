
import pytest
from isort.settings import Config

def test_skips():
    config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'buck-out', '.venv', '__pypackages__', '.bzr', '.'}))
    assert isinstance(config.skips(), frozenset)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_skips_1_test_invalid_inputs
isort/Test4DT_tests/test_isort_settings_Config_skips_1_test_invalid_inputs.py:7:22: E1102: config.skips is not callable (not-callable)


"""