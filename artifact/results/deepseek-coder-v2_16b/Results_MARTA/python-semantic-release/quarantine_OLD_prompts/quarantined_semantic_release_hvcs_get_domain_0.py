
import pytest
from unittest.mock import patch
from semantic_release.hvcs import get_hvcs
from semantic_release.exceptions import ImproperConfigurationError

def test_get_domain_valid_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock_get_hvcs:
        mock_get_hvcs.return_value.domain.return_value = "example.com"
        assert get_domain() == "example.com"

def test_get_domain_invalid_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock_get_hvcs:
        mock_get_hvcs.side_effect = ImproperConfigurationError("Invalid HVCS")
        with pytest.raises(ImproperConfigurationError):
            get_domain()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_________ ERROR collecting test_semantic_release_hvcs_get_domain_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_domain_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_domain_0.py:5: in <module>
    from semantic_release.exceptions import ImproperConfigurationError
E   ModuleNotFoundError: No module named 'semantic_release.exceptions'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_domain_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.33s ===============================
"""