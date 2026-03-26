
import pytest
from codetiming import Timer

def test_edge_cases():
    # Test None and empty values for optional parameters
    
    # Test with all optional parameters set to their default or None values
    timer = Timer()
    assert timer.name is None
    assert timer.text == 'Elapsed time: {:0.4f} seconds'
    assert not timer.initial_text  # This should be False, not a string comparison
    assert timer.logger == print
    
    # Test with name set to None
    timer_none_name = Timer(name=None)
    assert timer_none_name.name is None
    
    # Test with text set to a callable function
    def custom_text_function(elapsed):
        return f'Custom time: {elapsed:.4f} seconds'
    timer_custom_text = Timer(text=custom_text_function)
    assert callable(timer_custom_text.text)
    
    # Test with initial_text set to True
    timer_true_initial_text = Timer(initial_text=True)
    assert timer_true_initial_text.initial_text == 'Timer started'  # Correct assertion for boolean value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None and empty values for optional parameters
    
        # Test with all optional parameters set to their default or None values
        timer = Timer()
        assert timer.name is None
        assert timer.text == 'Elapsed time: {:0.4f} seconds'
        assert not timer.initial_text  # This should be False, not a string comparison
        assert timer.logger == print
    
        # Test with name set to None
        timer_none_name = Timer(name=None)
        assert timer_none_name.name is None
    
        # Test with text set to a callable function
        def custom_text_function(elapsed):
            return f'Custom time: {elapsed:.4f} seconds'
        timer_custom_text = Timer(text=custom_text_function)
        assert callable(timer_custom_text.text)
    
        # Test with initial_text set to True
        timer_true_initial_text = Timer(initial_text=True)
>       assert timer_true_initial_text.initial_text == 'Timer started'  # Correct assertion for boolean value
E       AssertionError: assert True == 'Timer started'
E        +  where True = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text=True, logger=<built-in function print>).initial_text

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.02s ===============================
"""