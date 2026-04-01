
import pytest
import inspect
import code
from unittest.mock import patch

def interact(banner='(debug shell)'):
    """
    Launch an interactive Python shell where the local variables of the caller's frame are available.
    
    This function creates a merged dictionary of global and local variables from the previous (calling) frame,
    then enters an interactive console session using the `code.interact` function with these variables.
    
    Parameters:
        banner (str): The banner text to display at the top of the interactive shell. Default is '(debug shell)'.
        
    Examples:
        >>> interact()
        Python 3.x (...some output...)
        >>> def test():
        ...     x = 10
        ...     y = 20
        ...     interact()
        ...
        >>> test()
        Python 3.x (...some output...)
        
    Notes:
        - The function uses `inspect` to get the current and previous frames.
        - It merges global and local variables from the calling frame for the interactive session.
        - The banner parameter allows customizing the displayed text at the start of the shell.
    
    Interactively explore the variables of the caller's frame in a Python shell.

    This function creates an interactive console that allows users to inspect and manipulate 
    the variables from the calling frame's global and local namespaces. The banner displayed 
    at the top of the console can be customized using the `banner` parameter.

    Parameters:
        banner (str): A string to display as the banner in the interactive shell. Default is '(debug shell)'.

    Returns:
        None
    """
    curr_frame = inspect.currentframe()

    try:
        calling_frame = curr_frame.f_back
        calling_vars = calling_frame.f_globals.copy()
        calling_vars.update(calling_frame.f_locals)
        code.interact(local=calling_vars, banner=banner)
    finally:
        del curr_frame

@pytest.fixture
def setup_interact():
    def _setup_interact(**kwargs):
        with patch('code.interact') as mock_interact:
            interact(**kwargs)
            return mock_interact
    return _setup_interact

@pytest.mark.parametrize("banner, expected_output", [
    ('Custom Banner', 'Python 3.x\nCustom Banner'),
    (None, 'Python 3.x\n(debug shell)')
])
def test_interact(setup_interact, banner, expected_output):
    mock_interact = setup_interact(banner=banner)
    
    # Capture the output of code.interact to verify it was called with the correct banner
    from io import StringIO
    captured_output = StringIO()
    import sys
    original_stdout = sys.stdout
    sys.stdout = captured_output
    
    interact(banner=banner)
    
    sys.stdout = original_stdout
    assert expected_output in captured_output.getvalue()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""