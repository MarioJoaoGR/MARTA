
import pytest
from unittest.mock import patch, MagicMock
from flutes.multiproc import ProgressBarManager

@pytest.mark.parametrize("verbose", [False])
def test_invalid_inputs(verbose):
    with patch('flutes.multiproc.ProgressBarManager._DummyProxy', new=MagicMock) as MockDummyProxy:
        mock_dummy_proxy = MockDummyProxy.return_value
        manager = ProgressBarManager(verbose=verbose, **{"incorrect": "kwargs"})

        # Test invalid kwargs
        with pytest.raises(ValueError):
            assert False  # This should not be reached if the exception is raised

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
__________________________ test_invalid_inputs[False] __________________________

verbose = False

    @pytest.mark.parametrize("verbose", [False])
    def test_invalid_inputs(verbose):
        with patch('flutes.multiproc.ProgressBarManager._DummyProxy', new=MagicMock) as MockDummyProxy:
            mock_dummy_proxy = MockDummyProxy.return_value
            manager = ProgressBarManager(verbose=verbose, **{"incorrect": "kwargs"})
    
            # Test invalid kwargs
            with pytest.raises(ValueError):
>               assert False  # This should not be reached if the exception is raised
E               assert False

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___1_test_invalid_inputs.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___1_test_invalid_inputs.py::test_invalid_inputs[False]
============================== 1 failed in 0.10s ===============================
"""