
import inspect
import code
import pytest

def interact(banner='(debug shell)'):
    """
    Launch an interactive Python shell where the local variables of the caller's frame are available.

    Parameters:
        banner (str, optional): The banner to display at the top of the interactive console. Default is '(debug shell)'.

    Description:
        This function creates a debug shell that allows you to interact with the local variables of the calling function. 
        It uses the `inspect` module to get the current and previous frames, then merges the global and local variables from the previous frame into a single dictionary.
        The interactive console (`code.interact`) is then launched with these merged variables as the local namespace, providing access to all the variables defined in the caller's scope.

    Example:
        def example_function():
            x = 10
            y = 20
            interact()
        
        In this example, calling `interact()` from within `example_function` will open an interactive shell where both `x` and `y` are available for inspection or manipulation.
    """
    curr_frame = inspect.currentframe()

    try:
        # Get previous frame (caller)
        calling_frame = curr_frame.f_back

        # Create merged dict of globals() with locals() from previous frame
        calling_vars = calling_frame.f_globals.copy()
        calling_vars.update(calling_frame.f_locals)

        # Enter interactive console
        code.interact(local=calling_vars, banner=banner)
    finally:
        del curr_frame

# Test edge cases for interact function
def test_edge_cases():
    with pytest.raises(TypeError):  # Banner should be a string or None
        interact(banner=None)  # Should raise TypeError because None is not a valid banner type
    
    with pytest.raises(TypeError):  # Banner should be a string or None
        interact(banner=12345)  # Should raise TypeError because int is not a valid banner type
    
    with pytest.raises(TypeError):  # Banner should be a string or None
        interact(banner=[1, 2, 3])  # Should raise TypeError because list is not a valid banner type
    
    with pytest.raises(TypeError):  # Banner should be a string or None
        interact(banner={'key': 'value'})  # Should raise TypeError because dict is not a valid banner type
    
    def test_function():
        x = 10
        y = 20
        interact()  # Default banner should work without issues
    
    with pytest.raises(TypeError):  # Banner should be a string or None
        interact(banner=None)  # Should raise TypeError because None is not a valid banner type

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

pytutils/Test4DT_tests/test_pytutils_debug_interact_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        with pytest.raises(TypeError):  # Banner should be a string or None
>           interact(banner=None)  # Should raise TypeError because None is not a valid banner type

pytutils/Test4DT_tests/test_pytutils_debug_interact_2_test_edge_cases.py:44: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/Test4DT_tests/test_pytutils_debug_interact_2_test_edge_cases.py:37: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f3028cb0710>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
>>> 
----------------------------- Captured stderr call -----------------------------
Python 3.11.15 (main, Mar 16 2026, 23:07:56) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_2_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""