
import pytest
from isort.place import _forced_separate, Config
from unittest.mock import MagicMock

def test_valid_input():
    config = MagicMock()
    config.forced_separate = ["*.log", "backup.*"]
    
    # Test case for a matching pattern
    result = _forced_separate("example.log", config)
    assert result == ('*.log', 'Matched forced_separate (*).log config value.')

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

isort/Test4DT_tests/test_isort_place__forced_separate_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        config = MagicMock()
        config.forced_separate = ["*.log", "backup.*"]
    
        # Test case for a matching pattern
        result = _forced_separate("example.log", config)
>       assert result == ('*.log', 'Matched forced_separate (*).log config value.')
E       AssertionError: assert ('*.log', 'Ma...onfig value.') == ('*.log', 'Ma...onfig value.')
E         
E         At index 1 diff: 'Matched forced_separate (*.log) config value.' != 'Matched forced_separate (*).log config value.'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_place__forced_separate_0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__forced_separate_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""