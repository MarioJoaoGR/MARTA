
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager(verbose=True)

def test_invalid_input(progress_bar_manager):
    # Test that the constructor raises an error when given invalid input
    with pytest.raises(ValueError):
        ProgressBarManager(verbose=False, invalid_arg='invalid')

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f5d676e3090>

    def test_invalid_input(progress_bar_manager):
        # Test that the constructor raises an error when given invalid input
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.13s ===============================
"""