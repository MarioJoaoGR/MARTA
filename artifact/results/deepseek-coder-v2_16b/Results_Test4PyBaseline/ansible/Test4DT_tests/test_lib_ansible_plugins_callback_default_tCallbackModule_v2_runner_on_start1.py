
import pytest
from ansible.plugins.callback import default

# Import the CallbackModule class from the specified module
CallbackModule = default.CallbackModule

def test_v2_runner_on_start_with_show_per_host_start(capsys):
    # Create an instance of CallbackModule
    callback = CallbackModule()
    
    # Set the option to enable display
    callback.set_option('show_per_host_start', True)
    
    # Define a mock host and task for testing
    host = "localhost"
    task = "echo 'Hello, World!'"
    
    # Call the method to be tested and capture the output
    callback.v2_runner_on_start(host, task)
    
    # Capture the standard output
    captured_output = capsys.readouterr()
    
    # Add assertions to validate the expected behavior
    assert " [started echo 'Hello, World!' on localhost]" in captured_output.out

def test_v2_runner_on_start_without_show_per_host_start(capsys):
    # Create an instance of CallbackModule
    callback = CallbackModule()
    
    # Set the option to disable display
    callback.set_option('show_per_host_start', False)
    
    # Define a mock host and task for testing
    host = "localhost"
    task = "echo 'Hello, World!'"
    
    # Call the method to be tested without capturing any output
    callback.v2_runner_on_start(host, task)
    
    # Capture the standard output
    captured_output = capsys.readouterr()
    
    # Add assertions to validate that no message is displayed
    assert " [started echo 'Hello, World!' on localhost]" not in captured_output.out
