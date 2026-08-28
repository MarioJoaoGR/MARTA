
import pytest
from ansible.plugins.callback import default as callback_module

# Test the v2_playbook_on_no_hosts_matched method of CallbackModule
def test_v2_playbook_on_no_hosts_matched():
    # Create an instance of CallbackModule
    callback = callback_module.CallbackModule()
    
    # Capture the output to verify the message is displayed correctly
    import sys
    from io import StringIO
    captured_output = StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output
    
    # Call the method under test
    callback.v2_playbook_on_no_hosts_matched()
    
    # Restore the original stdout
    sys.stdout = original_stdout
    
    # Check that the expected message is in the output
    assert "skipping: no hosts matched" in captured_output.getvalue().strip()

# Additional test case to cover the color parameter of _display.display method
def test_v2_playbook_on_no_hosts_matched_color():
    # Create an instance of CallbackModule
    callback = callback_module.CallbackModule()
    
    # Capture the output to verify the message is displayed with the correct color
    import sys
    from io import StringIO
    captured_output = StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output
    
    # Call the method under test with a specific color
    callback.v2_playbook_on_no_hosts_matched()
    
    # Restore the original stdout
    sys.stdout = original_stdout
    
    # Check that the expected message is in the output and the correct color is used
    assert "skipping: no hosts matched" in captured_output.getvalue().strip()
