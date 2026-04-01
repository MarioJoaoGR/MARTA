
import sys
import io
from unittest.mock import patch
from pytutils.debug import interact

def example_function():
    x = 10
    y = 20
    interact()

def test_valid_inputs():
    # Redirect stdout to a buffer so we can capture the output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    with patch('builtins.input', side_effect=['exit']):  # Mock input function for 'exit' command
        example_function()
    
    # Reset redirect.
    sys.stdout = sys.__stdout__
    
    # Check the output
    assert captured_output.getvalue().strip() == '(debug shell)'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_debug_interact_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Redirect stdout to a buffer so we can capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output
    
        with patch('builtins.input', side_effect=['exit']):  # Mock input function for 'exit' command
>           example_function()

pytutils/Test4DT_tests/test_pytutils_debug_interact_1_test_valid_inputs.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/Test4DT_tests/test_pytutils_debug_interact_1_test_valid_inputs.py:10: in example_function
    interact()
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='input' id='140623642770064'>, args = ('>>> ',)
kwargs = {}, effect = <list_iterator object at 0x7fe57e449060>

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
                raise effect
            elif not _callable(effect):
>               result = next(effect)
E               StopIteration

/usr/local/lib/python3.11/unittest/mock.py:1185: StopIteration
----------------------------- Captured stderr call -----------------------------
(debug shell)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.12s ===============================
"""