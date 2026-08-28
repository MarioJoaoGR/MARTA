
import pytest
from thefuck.already_configured import already_configured

@pytest.fixture
def mock_configuration_details():
    return {'reload': 'source ~/.bashrc'}

def test_already_configured(mock_configuration_details):
    expected_output = (
        "Seems like fuck alias already configured!\n"
        "For applying changes run source ~/.bashrc or restart your shell."
    )
    with pytest.raises(SystemExit) as excinfo:
        already_configured(mock_configuration_details)
    assert str(excinfo.value) == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________ ERROR collecting test_thefuck_logs_already_configured_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_logs_already_configured_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_logs_already_configured_0.py:3: in <module>
    from thefuck.already_configured import already_configured
E   ModuleNotFoundError: No module named 'thefuck.already_configured'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_logs_already_configured_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""