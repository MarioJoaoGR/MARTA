
import pytest
from isort.settings import Config

def test_config_init_with_none():
    with pytest.raises(TypeError):
        Config(config=None)

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

isort/Test4DT_tests/test_isort_settings_Config_skips_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
__________________________ test_config_init_with_none __________________________

    def test_config_init_with_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_settings_Config_skips_1_test_edge_cases.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_skips_1_test_edge_cases.py::test_config_init_with_none
============================== 1 failed in 0.13s ===============================
"""