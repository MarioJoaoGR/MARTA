
import pytest
from unittest.mock import patch, MagicMock
from flutes.multiproc import ProgressBarManager

class TestProgressBarManager:
    @patch('flutes.multiproc.ProgressBarManager._DummyProxy', autospec=True)
    def test_invalid_inputs(self, mock_dummy_proxy):
        # Arrange
        manager = ProgressBarManager()
    
        # Act & Assert
        with pytest.raises(ValueError):
            assert False, "Expected ValueError but did not raise"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
__________________ TestProgressBarManager.test_invalid_inputs __________________

self = <Test4DT_tests.test_flutes_multiproc_ProgressBarManager___init___1_test_invalid_inputs.TestProgressBarManager object at 0x7f2133502410>
mock_dummy_proxy = <MagicMock name='_DummyProxy' spec='_DummyProxy' id='139780567992208'>

    @patch('flutes.multiproc.ProgressBarManager._DummyProxy', autospec=True)
    def test_invalid_inputs(self, mock_dummy_proxy):
        # Arrange
        manager = ProgressBarManager()
    
        # Act & Assert
        with pytest.raises(ValueError):
>           assert False, "Expected ValueError but did not raise"
E           AssertionError: Expected ValueError but did not raise
E           assert False

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___1_test_invalid_inputs.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___1_test_invalid_inputs.py::TestProgressBarManager::test_invalid_inputs
============================== 1 failed in 0.13s ===============================
"""